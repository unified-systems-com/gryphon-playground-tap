# Changelog

## [0.6.7](https://github.com/unified-systems-com/gryphon-playground-tap/compare/v0.6.6...v0.6.7) (2026-11-25)


### Bug Fixes

* **boot:** ci record's grid_fixtures commit matches v0.3.6 ([dbeea62](https://github.com/unified-systems-com/gryphon-playground-tap/commit/dbeea6220b4e6cc328cc977722b1086ff760a2af))
* **boot:** pin grid_fixtures v0.3.6 (GRIFT format "1") in all three records ([afdc32c](https://github.com/unified-systems-com/gryphon-playground-tap/commit/afdc32ca61eaa8dc20ce7f7ed7f697836b044379))
* **boot:** pin grid_fixtures v0.3.6 (GRIFT format "1") in all three records ([91371ca](https://github.com/unified-systems-com/gryphon-playground-tap/commit/91371cac3327af403cd0ea3e68635503858f27fd))

## [0.6.6](https://github.com/unified-systems-com/gryphon-playground-tap/compare/v0.6.5...v0.6.6) (2026-11-25)


### Bug Fixes

* **grift:** seed fuzz graphs with the format "1" header from build_header ([666a7b8](https://github.com/unified-systems-com/gryphon-playground-tap/commit/666a7b8aeb9325cffadb2b6fa62a7c493f409ab9))
* **grift:** seed fuzz graphs with the format "1" header from build_header ([c71c7e2](https://github.com/unified-systems-com/gryphon-playground-tap/commit/c71c7e23f2d5226f56f12d43787314d45f1eae4c))

## [0.6.5](https://github.com/unified-systems-com/gryphon-playground-tap/compare/v0.6.4...v0.6.5) (2026-11-24)


### Bug Fixes

* move onto core v0.4.9 and restamp the wildcard-edge fixtures ([e327ec4](https://github.com/unified-systems-com/gryphon-playground-tap/commit/e327ec4fb4d4948fb34f044342f78c50b94bc97d))
* regenerate the Gridkin oracles and restamp GRIFT for core v0.4.9 ([d367986](https://github.com/unified-systems-com/gryphon-playground-tap/commit/d36798620dc195e4c3ae94a2286488ac353a1757))
* regenerate the Gridkin oracles for the spine copies and restamp GRIFT at format "1" ([43414ae](https://github.com/unified-systems-com/gryphon-playground-tap/commit/43414aeb2fb1048ea278e11a765e8dfd14e41400))

## [0.6.4](https://github.com/unified-systems-com/gryphon-playground-tap/compare/v0.6.3...v0.6.4) (2026-11-20)


### Features

* **dimensions:** seed the zone dimension; Gridkin snapshots for UUID-keyed dimensions ([7166f56](https://github.com/unified-systems-com/gryphon-playground-tap/commit/7166f560c47d56158c4f4615907b5615cc698c83))
* **dimensions:** seed the zone dimension; Gridkin snapshots for UUID-keyed dimensions ([647679c](https://github.com/unified-systems-com/gryphon-playground-tap/commit/647679caabd7e8025c3fb04b01af21442b5391c8))


### Bug Fixes

* **gridkin:** a snapshot holds the fixture's rows, not the grid's resident ones ([b80f3e0](https://github.com/unified-systems-com/gryphon-playground-tap/commit/b80f3e02ed1022f66e66c5331788c98c3364257f))
* **gridkin:** the oracle models the nodes already on the grid ([22dd9fe](https://github.com/unified-systems-com/gryphon-playground-tap/commit/22dd9fe44693d46410e1edd61cea1f0444d90b52))

## [0.6.3](https://github.com/unified-systems-com/gryphon-playground-tap/compare/v0.6.2...v0.6.3) (2026-10-30)


### Features

* **gridkin:** MIN and MAX scenarios, oracle and fuzz coverage ([#49](https://github.com/unified-systems-com/gryphon-playground-tap/issues/49)) ([8f47fd7](https://github.com/unified-systems-com/gryphon-playground-tap/commit/8f47fd77ded131c6ca74314e88786e625564f5ba))
* **gridkin:** negative-offset and hours-parameter scenarios; oracle refuses an unbound temporal base ([089dbaf](https://github.com/unified-systems-com/gryphon-playground-tap/commit/089dbaf6eaf28bd2e0610cb043f7029f99f14a64))
* **gridkin:** node-only COUNT, MIN and MAX scenarios and fuzz coverage [via rampart-pg] ([#50](https://github.com/unified-systems-com/gryphon-playground-tap/issues/50)) ([17c8e46](https://github.com/unified-systems-com/gryphon-playground-tap/commit/17c8e46c81e18c023af4e9eb8907ac371c9be91a))
* **gridkin:** temporal offset scenarios, scenario clock, oracle and fuzz coverage ([c336507](https://github.com/unified-systems-com/gryphon-playground-tap/commit/c3365071ae00899a7227364518955fce0431d344))
* **gridkin:** temporal offset scenarios, scenario clock, oracle and fuzz coverage [via gryphon-date-arith] ([402d780](https://github.com/unified-systems-com/gryphon-playground-tap/commit/402d7808f061a4d3f713e0d6eb65562126fba7d8))
* **gridkin:** the oracle refuses a RETURN item no MATCH clause binds [via gryphon-date-arith] ([d3a5544](https://github.com/unified-systems-com/gryphon-playground-tap/commit/d3a5544b71af9bf4cb9b2105cbd6a9232f8dabb2))
* **gridkin:** the oracle refuses a RETURN item no MATCH clause binds; rejection scenarios ([aefa486](https://github.com/unified-systems-com/gryphon-playground-tap/commit/aefa4869fd3e1064d499277a2c242ed19dd14672))
* **gridkin:** the oracle refuses a WHERE leaf no MATCH clause binds [via gryphon-date-arith] ([1870363](https://github.com/unified-systems-com/gryphon-playground-tap/commit/18703638231fb489c452411e47b85d592ea83bcf))
* **gridkin:** the oracle refuses a WHERE leaf no MATCH clause binds; rejection scenarios ([89b4645](https://github.com/unified-systems-com/gryphon-playground-tap/commit/89b4645c229940bd8aff2f35cd2458b38b0210ed))


### Bug Fixes

* **ci:** drop the stale contents: write grant past tap[#822](https://github.com/unified-systems-com/gryphon-playground-tap/issues/822) ([#45](https://github.com/unified-systems-com/gryphon-playground-tap/issues/45)) ([924f937](https://github.com/unified-systems-com/gryphon-playground-tap/commit/924f9378bce562d87bde2f21a29ab7501f757f0a))
* **ci:** restore contents: read on the plugin-ci caller job ([6e7e929](https://github.com/unified-systems-com/gryphon-playground-tap/commit/6e7e92958b4610b1eabc58c107dbb323a595f9bf))
* **ci:** restore contents: read on the plugin-ci caller job [via bom-bom] ([04f9e63](https://github.com/unified-systems-com/gryphon-playground-tap/commit/04f9e638fb64909c25e1b106e57306d207cc04d4))
* **gridkin:** registry redaction survives non-literal params; lock duplicate-key and bare dimension behaviour [via codex-security] ([#57](https://github.com/unified-systems-com/gryphon-playground-tap/issues/57)) ([dea3506](https://github.com/unified-systems-com/gryphon-playground-tap/commit/dea35068cb36d5e8b569812d614505a2a38bd62a))
* **nightly:** the CODEOWNERS this comment cited was removed today ([9e22380](https://github.com/unified-systems-com/gryphon-playground-tap/commit/9e223809316e2e9afa68003d4b7fc4f034efdd50))
