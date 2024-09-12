plugins {
    id("java")
    id("jacoco")
    id("checkstyle")
}

group = "northeastern.cs6510F2024"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    testImplementation(platform("org.junit:junit-bom:5.10.0"))
    testImplementation("org.junit.jupiter:junit-jupiter")
}

tasks.test {
    useJUnitPlatform()

    finalizedBy(tasks.jacocoTestReport) // JaCoCo should run after tests
}

// Jacoco Configuration
jacoco {
    toolVersion = "0.8.8"
}

tasks.jacocoTestReport {
    dependsOn(tasks.test) // Tests should run before generating the report

    reports {
        xml.required.set(true)  // Generates the XML report (useful for CI tools)
        html.required.set(true) // Generates the HTML report (viewable in a browser)
    }
}

tasks.jacocoTestCoverageVerification {
    dependsOn(tasks.jacocoTestReport) // Ensure that report is generated before verification

    violationRules {
        rule {
            isEnabled = true
            element = "CLASS"

            limit {
                counter = "LINE"
                minimum = "0.8".toBigDecimal() // Minimum threshold for coverage is 80%
            }
        }
    }
}

tasks.check {
    dependsOn(tasks.jacocoTestCoverageVerification)
}

tasks.withType<JavaCompile> {
    options.encoding = "UTF-8"
}

// Javadoc Configuration
tasks.javadoc {
    options {
        encoding = "UTF-8"
        (this as StandardJavadocDocletOptions).addStringOption("Xdoclint:none", "-quiet")
        isFailOnError = false // Set to true if Javadoc warnings should fail the build
    }
}

// CheckStyle Configuration
checkstyle {
    toolVersion = "10.18.0"
    configFile = file("config/checkstyle/checkstyle.xml")
}

tasks.checkstyleMain {
    source = sourceSets["main"].allJava // Set the source files for CheckStyle
}

tasks.checkstyleTest {
    source = sourceSets["test"].allJava // Optionally enforce CheckStyle on test files
}

tasks.withType<Checkstyle> {
    reports {
        xml.required.set(true)  // Generate XML reports (useful for CI)
        html.required.set(true) // Generate HTML reports for viewing
    }
}

// Custom task to run all tasks in sequence
tasks.register("doAll") {
    group = "custom"
    description = "Runs build, test, checkstyle, and javadoc in sequence."

    dependsOn(tasks.build)
    dependsOn(tasks.test)
    dependsOn(tasks.check)
    dependsOn(tasks.javadoc)

    doLast {
        println("All done!")
    }
}