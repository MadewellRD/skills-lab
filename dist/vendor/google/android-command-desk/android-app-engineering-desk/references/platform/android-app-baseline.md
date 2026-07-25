# Android App Development Baseline

Use this reference when an Android app workflow needs implementation or review defaults and the repo does not supply a stronger local convention.

## Preferred modern app lane
- Kotlin first, Java supported when existing repo state requires it.
- Jetpack Compose for new UI when the repo already uses Compose or migration is explicitly accepted.
- Existing View/XML patterns remain authoritative for legacy apps unless migration is in scope.
- Modularization should follow source evidence from Gradle settings, module ownership, and dependency boundaries.
- DI, data layer, offline/sync, background work, and permissions must be explicit before implementation handoff.
- Screenshot/UI tests, instrumented tests, Macrobenchmark, and Baseline Profiles are release-quality gates when relevant to the requested scope.

## Evidence to collect
- `settings.gradle(.kts)`, root/module `build.gradle(.kts)`, version catalogs, Gradle wrapper, AGP/Kotlin versions
- `AndroidManifest.xml`, permissions, exported components, app links, services, receivers, providers
- source modules, package/application ID, build variants/flavors, CI workflows, test tasks
- existing architecture docs, navigation files, Compose/View usage, data/storage/network code

## Halt triggers
- no repo/module target for implementation
- target SDK/min SDK/compile SDK affects scope but is unknown
- permissions, data collection, signing, Play policy, or release state is required but unresolved
- no validation command can be identified
