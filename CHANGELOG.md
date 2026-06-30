# Changelog

## [4.164.0](https://github.com/team-telnyx/telnyx-python/compare/v4.163.1...v4.164.0) (2026-06-30)


### Bug Fixes

* add --local flag so release-please scans next branch for commits ([#343](https://github.com/team-telnyx/telnyx-python/issues/343)) ([be71009](https://github.com/team-telnyx/telnyx-python/commit/be7100906c7ce107c0aca9b8197b6fff5e5af0ec))
* **release-please:** restore version files after -X theirs merge ([#340](https://github.com/team-telnyx/telnyx-python/issues/340)) ([8d15e8e](https://github.com/team-telnyx/telnyx-python/commit/8d15e8ea6be01cc35370ba71fdba951f9ae93b24))


### Chores

* remove leaked staging-only promote-to-prod.yml from prod ([#346](https://github.com/team-telnyx/telnyx-python/issues/346)) ([addb7ca](https://github.com/team-telnyx/telnyx-python/commit/addb7ca8e8701ecf6c391a1e1ca273a5c0441524))

## [4.163.2](https://github.com/team-telnyx/telnyx-python/compare/v4.163.1...v4.163.2) (2026-06-23)


### Bug Fixes

* **release-please:** restore version files after -X theirs merge ([#340](https://github.com/team-telnyx/telnyx-python/issues/340)) ([8d15e8e](https://github.com/team-telnyx/telnyx-python/commit/8d15e8ea6be01cc35370ba71fdba951f9ae93b24))

## [4.162.1](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.162.0...v4.162.1) (2026-06-22)


### Bug Fixes

* restore promote-to-prod.yml workflow ([cafbafa](https://github.com/team-telnyx/telnyx-python-staging/commit/cafbafa02649a08f33e1f8631c013be05b54bf88))

## [4.162.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.161.1...v4.162.0) (2026-06-22)


### Bug Fixes

* remove stale imports for deleted types ([0f5c80b](https://github.com/team-telnyx/telnyx-python-staging/commit/0f5c80bc605773e349618e9a7dfd47b0ea1ee690))
* restore TYPE_CHECKING import and remove None guard in preserved files ([e9d9375](https://github.com/team-telnyx/telnyx-python-staging/commit/e9d9375b322f85632bf7ebf1cd6dbf1032783add))


### Chores

* preserve repo-owned files not part of SDK generation ([876026e](https://github.com/team-telnyx/telnyx-python-staging/commit/876026ebe9fa402f625417d6b35314ab2c0ccfee))
* release python 4.162.0 ([1f1c960](https://github.com/team-telnyx/telnyx-python-staging/commit/1f1c9603d45c75f08cb431a02459a56abc59aabc))
* remove stale files from previous generation ([db377be](https://github.com/team-telnyx/telnyx-python-staging/commit/db377befde2d3d1b605e21c661175ec567c16d36))

## [4.161.1](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.161.0...v4.161.1) (2026-06-22)


### Bug Fixes

* **ci:** add test job to staging CI to match prod ([039286b](https://github.com/team-telnyx/telnyx-python-staging/commit/039286bb93ca9c96aebf03138683a815d378ac32))
* **ci:** add test job to staging CI to match prod ([1d0bc11](https://github.com/team-telnyx/telnyx-python-staging/commit/1d0bc1135f1dad9fcef0f89f7259646a62dca3fe))
* **types:** resolve circular import in texml recordings response body ([84b7ae4](https://github.com/team-telnyx/telnyx-python-staging/commit/84b7ae432c965240ce91c05d4de043d473636063))

## [4.161.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.160.0...v4.161.0) (2026-06-22)


### Bug Fixes

* restore deleted type files to fix mypy import errors ([1a0e359](https://github.com/team-telnyx/telnyx-python-staging/commit/1a0e3596152be9982574615b6e21bd0c501384af))
* restore dir_retrieve_document_types_response.py ([7ffd1d6](https://github.com/team-telnyx/telnyx-python-staging/commit/7ffd1d63414f3fa3d69d8069b61c946206b41609))
* restore dir_retrieve_infringement_claims_response.py ([001ce04](https://github.com/team-telnyx/telnyx-python-staging/commit/001ce044ba388b4abbb8dccd010851d689a5b8c3))


### Chores

* add promote-to-prod workflow and fix prerelease config ([5b616aa](https://github.com/team-telnyx/telnyx-python-staging/commit/5b616aa0b946f40bc833db7de69f9831ce371a67))
* add promote-to-prod.yml + remove prerelease config ([b97c239](https://github.com/team-telnyx/telnyx-python-staging/commit/b97c239fe6c539d3a64f0c401a408bbac66b9b98))
* preserve repo-owned files not part of SDK generation ([847a466](https://github.com/team-telnyx/telnyx-python-staging/commit/847a46693c350cf931f3decc407da2c709fe6b82))
* release python 4.161.0 ([86d5b64](https://github.com/team-telnyx/telnyx-python-staging/commit/86d5b64c8ad3fdec9fb6e7c72c15143c513d59fe))
* remove stale files from previous generation ([faffa38](https://github.com/team-telnyx/telnyx-python-staging/commit/faffa3839f32371124893b3715e621a9426cfae1))

## [4.160.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.159.0...v4.160.0) (2026-06-18)


### Chores

* preserve repo-owned files not part of SDK generation ([3eaf0b1](https://github.com/team-telnyx/telnyx-python-staging/commit/3eaf0b14bd8d9917a9c48d5d6acc3d5a3561c341))
* release python 4.160.0 ([fc25537](https://github.com/team-telnyx/telnyx-python-staging/commit/fc25537b503fb4e87cbfc2c8784c36b11bfa1109))
* sync OpenAPI spec from cde0bc4 ([b8c35eb](https://github.com/team-telnyx/telnyx-python-staging/commit/b8c35eb0c4a59fee2280e1c4806fc3b77211d49e))
* sync OpenAPI spec from cde0bc4 ([1d541f0](https://github.com/team-telnyx/telnyx-python-staging/commit/1d541f0346711191fcc24a15a9743827e0fe6fbd))

## [4.159.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.158.0...v4.159.0) (2026-06-18)


### Chores

* preserve repo-owned files not part of SDK generation ([9edbc94](https://github.com/team-telnyx/telnyx-python-staging/commit/9edbc941961909af20b2c4d87ffbc423437360fe))
* release python 4.159.0 ([a3533df](https://github.com/team-telnyx/telnyx-python-staging/commit/a3533dfb5d710f4ce0a4a764c5b9ab35750b726e))
* sync OpenAPI spec from 18f622e ([e2d0006](https://github.com/team-telnyx/telnyx-python-staging/commit/e2d000696b4b5c8a4903324d040c6551befe1944))
* sync OpenAPI spec from 18f622e ([a34242a](https://github.com/team-telnyx/telnyx-python-staging/commit/a34242aa4cc23989e53a6a2b1c5c2bc0bec912fb))

## [4.158.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.157.0...v4.158.0) (2026-06-18)


### Bug Fixes

* update transforms for inlined response schemas ([2a1fef9](https://github.com/team-telnyx/telnyx-python-staging/commit/2a1fef9d3f4d255e64888dbf9390067064a12832))
* update transforms for inlined response schemas ([4d28007](https://github.com/team-telnyx/telnyx-python-staging/commit/4d28007757e0649773cb36c58fb3988fac052d23))


### Chores

* preserve repo-owned files not part of SDK generation ([1b5b215](https://github.com/team-telnyx/telnyx-python-staging/commit/1b5b215a0ff7f8509803551f1cd10bf156ddba17))
* release python 4.158.0 ([ee068c4](https://github.com/team-telnyx/telnyx-python-staging/commit/ee068c463effeacdd45be33e8c030db20abc95ee))

## [4.157.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.156.0...v4.157.0) (2026-06-16)


### Chores

* preserve repo-owned files not part of SDK generation ([10c80a0](https://github.com/team-telnyx/telnyx-python-staging/commit/10c80a0070dee50258bc2bf7ce4815f4682c29d4))
* release python 4.157.0 ([d5b87b7](https://github.com/team-telnyx/telnyx-python-staging/commit/d5b87b780203aa1493b8f84bb4571903fcd7d1ca))

## [4.156.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.155.0...v4.156.0) (2026-06-16)


### Chores

* preserve repo-owned files not part of SDK generation ([be516d9](https://github.com/team-telnyx/telnyx-python-staging/commit/be516d9f71977aaf5b958c0b4f3db682ecd4833f))
* release python 4.156.0 ([1d81a2d](https://github.com/team-telnyx/telnyx-python-staging/commit/1d81a2d20c9ed1d6cbf629fb4a3c20a19e34ea44))

## [4.155.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.154.0...v4.155.0) (2026-06-16)


### Chores

* preserve repo-owned files not part of SDK generation ([4fee0f0](https://github.com/team-telnyx/telnyx-python-staging/commit/4fee0f011d30703548107cfb4f87ef30d999ee07))
* release python 4.155.0 ([1881884](https://github.com/team-telnyx/telnyx-python-staging/commit/1881884e30bf53afad6c7670f483d9e4b73f53bc))
* sync OpenAPI spec from e44bbbc ([7331dc7](https://github.com/team-telnyx/telnyx-python-staging/commit/7331dc77d3c6490ef411b89fd375b5c977c3841a))
* sync OpenAPI spec from e44bbbc ([1fdce1c](https://github.com/team-telnyx/telnyx-python-staging/commit/1fdce1c885f5955b0b8f79e89e132c051deb8af3))

## [4.154.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.153.0...v4.154.0) (2026-06-15)


### Bug Fixes

* rename DIR method names to match published SDKs ([8b47978](https://github.com/team-telnyx/telnyx-python-staging/commit/8b4797804f94025ce845b7e356ba9b73a810789a))
* rename DIR method names to match published SDKs ([8348139](https://github.com/team-telnyx/telnyx-python-staging/commit/8348139162421b2f58dce1dab781f56d76787e64))


### Chores

* preserve repo-owned files not part of SDK generation ([f37648b](https://github.com/team-telnyx/telnyx-python-staging/commit/f37648b4913b63249d6a54cad3e7d948071dfaf7))
* release python 4.154.0 ([4b813c3](https://github.com/team-telnyx/telnyx-python-staging/commit/4b813c3422c6e862c714d36a7f538dc5f19cebc5))

## [4.153.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.152.0...v4.153.0) (2026-06-15)


### Chores

* preserve repo-owned files not part of SDK generation ([5d93a75](https://github.com/team-telnyx/telnyx-python-staging/commit/5d93a757b5b924d6120c3d0d2b0c39c34d12008b))
* release python 4.153.0 ([483d685](https://github.com/team-telnyx/telnyx-python-staging/commit/483d68518420398eeb7e19c86095df5e226ce383))
* sync OpenAPI spec from 3b5c722 ([4d4b975](https://github.com/team-telnyx/telnyx-python-staging/commit/4d4b97506fe125704cbcd8c1edcc948049280754))
* sync OpenAPI spec from 3b5c722 ([daef305](https://github.com/team-telnyx/telnyx-python-staging/commit/daef305b81bc32c3b4a4a3bc2e30582fe49545fe))

## [4.152.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.151.0...v4.152.0) (2026-06-10)


### Chores

* preserve repo-owned files not part of SDK generation ([7d5b6a6](https://github.com/team-telnyx/telnyx-python-staging/commit/7d5b6a6094d6015f66a7ef0bd2485c93f4df0cf1))
* release python 4.152.0 ([d011493](https://github.com/team-telnyx/telnyx-python-staging/commit/d011493e0d14323b764594243fbbd00dc857259f))
* sync OpenAPI spec from b9f127e ([344ccda](https://github.com/team-telnyx/telnyx-python-staging/commit/344ccda27799521ce819cf25eb0f0b73ea1e429a))
* sync OpenAPI spec from b9f127e ([b8b51f7](https://github.com/team-telnyx/telnyx-python-staging/commit/b8b51f76defafbdc46fbfb334a56eeb5eaa90445))

## [4.151.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.150.0...v4.151.0) (2026-06-09)


### Chores

* preserve repo-owned files not part of SDK generation ([0918186](https://github.com/team-telnyx/telnyx-python-staging/commit/0918186b22c4dc98b1cfdcd9732909c8e010d4ed))
* release python 4.151.0 ([1340cae](https://github.com/team-telnyx/telnyx-python-staging/commit/1340caeb356e65fd82bf2cc682aa432cf627a454))
* sync OpenAPI spec from 2677196 ([5dc39a4](https://github.com/team-telnyx/telnyx-python-staging/commit/5dc39a454fecd8e09c46e9fadd374c33c7647005))
* sync OpenAPI spec from 2677196 ([cf0038d](https://github.com/team-telnyx/telnyx-python-staging/commit/cf0038d07c28f79ba1e2e382f6636882a7ded429))

## [4.150.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.149.0...v4.150.0) (2026-06-09)


### Chores

* preserve repo-owned files not part of SDK generation ([05b428a](https://github.com/team-telnyx/telnyx-python-staging/commit/05b428aa8f823cb33be825cca8a55f5392a2d887))
* release python 4.150.0 ([c0bfa0a](https://github.com/team-telnyx/telnyx-python-staging/commit/c0bfa0ad566fb8ef1564c4357ecf3747cca07eeb))
* sync OpenAPI spec from c319cee ([68fc585](https://github.com/team-telnyx/telnyx-python-staging/commit/68fc585d05a8567ba2ddf23fc8e494c144213885))
* sync OpenAPI spec from c319cee ([11d11e0](https://github.com/team-telnyx/telnyx-python-staging/commit/11d11e0c635f093ffd93e98afe241950a8fca68e))

## [4.149.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.148.0...v4.149.0) (2026-06-09)


### Chores

* dedupe imports in types/__init__.py to satisfy ruff lint ([ad480b2](https://github.com/team-telnyx/telnyx-python-staging/commit/ad480b2857130a0e71f415e8eee4709159e91a69))
* preserve repo-owned files not part of SDK generation ([c6907b7](https://github.com/team-telnyx/telnyx-python-staging/commit/c6907b7a0a3def18b36823a20358cd9c9bfe9725))
* release python 4.149.0 ([7545d56](https://github.com/team-telnyx/telnyx-python-staging/commit/7545d56bbcf99f02e8c4100e34c8713513025166))
* sync OpenAPI spec from aae7c19 ([52417da](https://github.com/team-telnyx/telnyx-python-staging/commit/52417daa841323303f4079251dc012e502304bdb))
* sync OpenAPI spec from aae7c19 ([e12d12a](https://github.com/team-telnyx/telnyx-python-staging/commit/e12d12aaee733a876ea2acc8cd75eb760893e8b1))

## [4.148.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.147.0...v4.148.0) (2026-06-08)


### Chores

* preserve repo-owned files not part of SDK generation ([dee6097](https://github.com/team-telnyx/telnyx-python-staging/commit/dee6097417a8b917ac8275ad4f9b051793eee0aa))
* release python 4.148.0 ([0be1567](https://github.com/team-telnyx/telnyx-python-staging/commit/0be1567fe746b0cdec24920ead12fabc38a5378c))
* sync OpenAPI spec from a13d4b1 ([d82de0f](https://github.com/team-telnyx/telnyx-python-staging/commit/d82de0f20054014319aa65aed3456c951727d38b))
* sync OpenAPI spec from a13d4b1 ([1d39e9a](https://github.com/team-telnyx/telnyx-python-staging/commit/1d39e9aba3480259e3d60ab908184d66b4971515))

## [4.147.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.146.0...v4.147.0) (2026-06-08)


### Chores

* preserve repo-owned files not part of SDK generation ([b2be483](https://github.com/team-telnyx/telnyx-python-staging/commit/b2be483f29a19b1e4befeeeced0f695ebc0618de))
* release python 4.147.0 ([af82347](https://github.com/team-telnyx/telnyx-python-staging/commit/af823477eda10ff8d3d194b07eab879bcbb7cc93))

## [4.146.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.145.0...v4.146.0) (2026-06-08)


### Bug Fixes

* rename loa methods patch_all/create → update/render to match upstream ([17d87f0](https://github.com/team-telnyx/telnyx-python-staging/commit/17d87f0ae8b0aca7eda843de1daee35014ba676d))
* rename loa methods patch_all/create → update/render to match upstream ([7457f4c](https://github.com/team-telnyx/telnyx-python-staging/commit/7457f4ca56ee8a54728916b765642638771c0221))


### Chores

* preserve repo-owned files not part of SDK generation ([2ffc98f](https://github.com/team-telnyx/telnyx-python-staging/commit/2ffc98fe3ba54c02c9fbd4b19eeafff1d2b96c26))
* release python 4.146.0 ([5ba7037](https://github.com/team-telnyx/telnyx-python-staging/commit/5ba703706088936da7cae8de21d939c39a3e96f9))

## [4.145.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.144.0...v4.145.0) (2026-06-08)


### Chores

* preserve repo-owned files not part of SDK generation ([edbab05](https://github.com/team-telnyx/telnyx-python-staging/commit/edbab0556e49199ca2ed96c92b5ad609c55b3472))
* release python 4.145.0 ([ba2af8a](https://github.com/team-telnyx/telnyx-python-staging/commit/ba2af8a38b1ae18905857b488cb6ef15143a32ce))

## [4.144.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.142.1...v4.144.0) (2026-06-08)


### Bug Fixes

* **ci:** pass release-please pr output via env to avoid shell injection ([6a008b0](https://github.com/team-telnyx/telnyx-python-staging/commit/6a008b03fe1571b40c6160808b114e45da08bf1f))
* **ci:** pass release-please pr output via env to avoid shell injection ([60a9709](https://github.com/team-telnyx/telnyx-python-staging/commit/60a9709627fc4f5ec6b7b7cc73051b3de832c3f8))
* remove agent_input model from loa subresource to fix duplicate TypeScript export ([a3952a7](https://github.com/team-telnyx/telnyx-python-staging/commit/a3952a78c23e3cc1c28d16ba03b86dec8308bd4d))
* remove agent_input model from loa subresource to fix duplicate TypeScript export ([80e94d9](https://github.com/team-telnyx/telnyx-python-staging/commit/80e94d952f39c2c3cedd260d23e83807b5a7bd44))


### Chores

* preserve repo-owned files not part of SDK generation ([8a39071](https://github.com/team-telnyx/telnyx-python-staging/commit/8a3907173f203e8488fcf11a19643c40e42208b8))
* preserve repo-owned files not part of SDK generation ([ba506b4](https://github.com/team-telnyx/telnyx-python-staging/commit/ba506b4291415354204afd9d15f93cb0dfc062f6))
* preserve repo-owned files not part of SDK generation ([7420d51](https://github.com/team-telnyx/telnyx-python-staging/commit/7420d51b41847ec26e3db2ae8f22a8847f6c6d1a))
* preserve repo-owned files not part of SDK generation ([d66d2b6](https://github.com/team-telnyx/telnyx-python-staging/commit/d66d2b6b74697cabc70a9392c70d3ebb60efa643))
* release python 4.143.0 ([9409310](https://github.com/team-telnyx/telnyx-python-staging/commit/940931074cb06555ef492fa60c4b9ea00493ff16))
* release python 4.143.0 ([7b1d436](https://github.com/team-telnyx/telnyx-python-staging/commit/7b1d4369da10276b7afb4b551369d94981667381))
* release python 4.143.0 ([a6e7046](https://github.com/team-telnyx/telnyx-python-staging/commit/a6e704643b3c75598c5fccda06ab2fd8064e1d8c))
* release python 4.144.0 ([b5b378f](https://github.com/team-telnyx/telnyx-python-staging/commit/b5b378f53ea9193e580014135be16df5d5ee3441))
* sync OpenAPI spec from 6eae6a5 ([387eeec](https://github.com/team-telnyx/telnyx-python-staging/commit/387eeec9cd7318ba95ba95bb1d76ed4cad2db04a))
* sync OpenAPI spec from 6eae6a5 ([7ea3b4a](https://github.com/team-telnyx/telnyx-python-staging/commit/7ea3b4a503f39ca8a695fc531536e60492c4d809))
* sync OpenAPI spec from 95f10ce ([b3ff600](https://github.com/team-telnyx/telnyx-python-staging/commit/b3ff600a1d285df71ce72c4b88f0c6ded67066b4))
* sync OpenAPI spec from 95f10ce ([8d957ea](https://github.com/team-telnyx/telnyx-python-staging/commit/8d957ea2b46f39c939c116b4f41298978bdcad9f))
* sync OpenAPI spec from 9f5f345 ([a4262e4](https://github.com/team-telnyx/telnyx-python-staging/commit/a4262e4b1e187e04ccd9dbf6d2cf323e23be29a1))
* sync OpenAPI spec from 9f5f345 ([8827c91](https://github.com/team-telnyx/telnyx-python-staging/commit/8827c9162282a95d181b1a6d7e4f61fc794fb28f))

## [4.143.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.142.1...v4.143.0) (2026-06-08)


### Bug Fixes

* **ci:** pass release-please pr output via env to avoid shell injection ([6a008b0](https://github.com/team-telnyx/telnyx-python-staging/commit/6a008b03fe1571b40c6160808b114e45da08bf1f))
* **ci:** pass release-please pr output via env to avoid shell injection ([60a9709](https://github.com/team-telnyx/telnyx-python-staging/commit/60a9709627fc4f5ec6b7b7cc73051b3de832c3f8))


### Chores

* preserve repo-owned files not part of SDK generation ([ba506b4](https://github.com/team-telnyx/telnyx-python-staging/commit/ba506b4291415354204afd9d15f93cb0dfc062f6))
* preserve repo-owned files not part of SDK generation ([7420d51](https://github.com/team-telnyx/telnyx-python-staging/commit/7420d51b41847ec26e3db2ae8f22a8847f6c6d1a))
* preserve repo-owned files not part of SDK generation ([d66d2b6](https://github.com/team-telnyx/telnyx-python-staging/commit/d66d2b6b74697cabc70a9392c70d3ebb60efa643))
* release python 4.143.0 ([9409310](https://github.com/team-telnyx/telnyx-python-staging/commit/940931074cb06555ef492fa60c4b9ea00493ff16))
* release python 4.143.0 ([7b1d436](https://github.com/team-telnyx/telnyx-python-staging/commit/7b1d4369da10276b7afb4b551369d94981667381))
* release python 4.143.0 ([a6e7046](https://github.com/team-telnyx/telnyx-python-staging/commit/a6e704643b3c75598c5fccda06ab2fd8064e1d8c))
* sync OpenAPI spec from 6eae6a5 ([387eeec](https://github.com/team-telnyx/telnyx-python-staging/commit/387eeec9cd7318ba95ba95bb1d76ed4cad2db04a))
* sync OpenAPI spec from 6eae6a5 ([7ea3b4a](https://github.com/team-telnyx/telnyx-python-staging/commit/7ea3b4a503f39ca8a695fc531536e60492c4d809))
* sync OpenAPI spec from 95f10ce ([b3ff600](https://github.com/team-telnyx/telnyx-python-staging/commit/b3ff600a1d285df71ce72c4b88f0c6ded67066b4))
* sync OpenAPI spec from 95f10ce ([8d957ea](https://github.com/team-telnyx/telnyx-python-staging/commit/8d957ea2b46f39c939c116b4f41298978bdcad9f))
* sync OpenAPI spec from 9f5f345 ([a4262e4](https://github.com/team-telnyx/telnyx-python-staging/commit/a4262e4b1e187e04ccd9dbf6d2cf323e23be29a1))
* sync OpenAPI spec from 9f5f345 ([8827c91](https://github.com/team-telnyx/telnyx-python-staging/commit/8827c9162282a95d181b1a6d7e4f61fc794fb28f))

## [4.142.1](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.142.0...v4.142.1) (2026-06-07)


### Bug Fixes

* extract PR number from JSON output for auto-merge ([e330da9](https://github.com/team-telnyx/telnyx-python-staging/commit/e330da9d2d3cfec405c3a0f7ba069dfe0bf667d6))
* extract PR number from JSON output for auto-merge ([9fac492](https://github.com/team-telnyx/telnyx-python-staging/commit/9fac4921529b62a9adfe7f1366ccd6439a70b758))
* use release-please output directly for auto-merge (avoid race condition) ([01bc872](https://github.com/team-telnyx/telnyx-python-staging/commit/01bc872ba23389f616f0f3993dea2e522218e0b8))
* use release-please output directly for auto-merge (avoid race condition) ([cc9f986](https://github.com/team-telnyx/telnyx-python-staging/commit/cc9f986e5111adeb1851d2ae1f9b24d5b4cae2a7))

## [4.142.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.141.0...v4.142.0) (2026-06-07)


### Chores

* preserve repo-owned files not part of SDK generation ([755d760](https://github.com/team-telnyx/telnyx-python-staging/commit/755d7607ad9fcca8a159c6c1a86ae15bf62e52a4))
* preserve repo-owned files not part of SDK generation ([bfdf0ab](https://github.com/team-telnyx/telnyx-python-staging/commit/bfdf0abb933360f64247e6511f22b8a48812d81f))
* release python 4.142.0 ([a5f798d](https://github.com/team-telnyx/telnyx-python-staging/commit/a5f798dcab4a4b4c69904f16dcd88a4f151a7c46))
* release python 4.142.0 ([94cd65a](https://github.com/team-telnyx/telnyx-python-staging/commit/94cd65a33412d34486e621e4a480e388fdb5f4b4))
* sync OpenAPI spec from 0193002 ([bb2a244](https://github.com/team-telnyx/telnyx-python-staging/commit/bb2a2446d33a93b287554e58fcf6d480d5ec6b11))
* sync OpenAPI spec from 0193002 ([8fefaf7](https://github.com/team-telnyx/telnyx-python-staging/commit/8fefaf7776c7ba11d8e18d9f0fa2f408f65a4311))
* sync OpenAPI spec from 8faa4be ([d335481](https://github.com/team-telnyx/telnyx-python-staging/commit/d33548196842d4ab2cd1d1296b43559f97bcbdee))
* sync OpenAPI spec from 8faa4be ([51f2211](https://github.com/team-telnyx/telnyx-python-staging/commit/51f2211469e30738650872b51078f3055e678fea))

## [4.141.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.140.0...v4.141.0) (2026-06-07)


### Features

* enable GitHub auto-merge on release PRs ([779a97e](https://github.com/team-telnyx/telnyx-python-staging/commit/779a97e8df2bebceb1e034911dc4a9c2bbfb01ca))
* enable GitHub auto-merge on release PRs ([3d10c26](https://github.com/team-telnyx/telnyx-python-staging/commit/3d10c262ecf1dd856f178a0d3f8a2c4b53ffd8d4))


### Bug Fixes

* correct auto-merge output name and PR search pattern ([a2258d1](https://github.com/team-telnyx/telnyx-python-staging/commit/a2258d1d3c3ea1b07c83500e6d0a16d348e51f53))
* correct auto-merge output name and PR search pattern ([1c4f1ed](https://github.com/team-telnyx/telnyx-python-staging/commit/1c4f1edf0ff29d0138d65a556aa87a458c6e217d))
* restore ${{ }} expressions in release-please workflow ([542a369](https://github.com/team-telnyx/telnyx-python-staging/commit/542a369ffa11ffaafeeedabd061f47a7ee455d7c))
* restore ${{ }} expressions in release-please workflow ([763a252](https://github.com/team-telnyx/telnyx-python-staging/commit/763a2522485ebee99c6118ed1b010020a8b3d038))

## [4.140.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.139.0...v4.140.0) (2026-06-07)


### Features

* enable automerge for release PRs ([df4506a](https://github.com/team-telnyx/telnyx-python-staging/commit/df4506ab97b9053ac9a36c5d53e66e8079965400))

## [4.139.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.138.1...v4.139.0) (2026-06-07)


### Bug Fixes

* merge fresh generated code with custom create_speech ([7a67a5a](https://github.com/team-telnyx/telnyx-python-staging/commit/7a67a5ac4221f3c02c50f4adced04d4c38992a63))
* update custom code to use generate_speech types ([33b8112](https://github.com/team-telnyx/telnyx-python-staging/commit/33b81120e35c273c85b85f67f44f753893594cb0))
* use PAT for release-please to trigger CI ([a82d3ed](https://github.com/team-telnyx/telnyx-python-staging/commit/a82d3eddb42ca0d6b11a5972f925f30a9a9fd9fa))
* use PAT for release-please to trigger CI ([d9ef834](https://github.com/team-telnyx/telnyx-python-staging/commit/d9ef8342ba6ea0706e2cd1446baabca9b0afe77e))


### Chores

* preserve repo-owned files not part of SDK generation ([ebb0679](https://github.com/team-telnyx/telnyx-python-staging/commit/ebb0679bc945c1edd16c75faaa3504b77fe17f05))
* release python 4.139.0 ([0e5b9ad](https://github.com/team-telnyx/telnyx-python-staging/commit/0e5b9ada6e73ba5eb47b7b146bf199a59e2a6fb3))

## [4.138.1](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.138.0...v4.138.1) (2026-06-05)


### Bug Fixes

* run CI build/lint on internal PRs not just forks ([f220675](https://github.com/team-telnyx/telnyx-python-staging/commit/f220675944515e5c8613d7959c1b483d8c168452))
* use consistent single quotes in CI if condition ([e783e55](https://github.com/team-telnyx/telnyx-python-staging/commit/e783e554cf11b6d6b13bf56563d5b0670e8c33da))
* use consistent single quotes in CI if condition ([9099d67](https://github.com/team-telnyx/telnyx-python-staging/commit/9099d675d13cca7b2b814377286acafb7b33c3c8))

## [4.138.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.137.0...v4.138.0) (2026-06-04)


### Chores

* release python 4.138.0 ([bc407ff](https://github.com/team-telnyx/telnyx-python-staging/commit/bc407ff18874f7a89d600209be8adfeb75d125c0))

## [4.137.0](https://github.com/team-telnyx/telnyx-python-staging/compare/v4.136.0...v4.137.0) (2026-06-03)


### Chores

* release python 4.137.0 ([cc15bee](https://github.com/team-telnyx/telnyx-python-staging/commit/cc15bee0617f3adac41e777137fbb65907cb12e8))
* sync OpenAPI spec from c2d3485 ([18bb6ce](https://github.com/team-telnyx/telnyx-python-staging/commit/18bb6ce7d3e65929fcf0298d3cd599f7ce81d451))

## 4.136.0 (2026-05-15)

Full Changelog: [v4.135.0...v4.136.0](https://github.com/team-telnyx/telnyx-python/compare/v4.135.0...v4.136.0)

### Features

* **api:** manual updates ([b60f39c](https://github.com/team-telnyx/telnyx-python/commit/b60f39c59eafd3fe80a26720e50e96e134fc44b2))

## 4.135.0 (2026-05-15)

Full Changelog: [v4.134.0...v4.135.0](https://github.com/team-telnyx/telnyx-python/compare/v4.134.0...v4.135.0)

### Features

* Document PremiumCallScreening detection mode ([77ffa1b](https://github.com/team-telnyx/telnyx-python/commit/77ffa1bd62e2b1454fc1e12079d740a06063a0b3))


### Documentation

* add supported file formats to Send Fax endpoint ([8f73895](https://github.com/team-telnyx/telnyx-python/commit/8f738952250095e0f421edbaae93ccfa2b26094b))

## 4.134.0 (2026-05-15)

Full Changelog: [v4.133.0...v4.134.0](https://github.com/team-telnyx/telnyx-python/compare/v4.133.0...v4.134.0)

### Features

* Update Conversation Relay start parameters ([2121536](https://github.com/team-telnyx/telnyx-python/commit/21215362636bf962851b75e80ff38d594812aa2e))

## 4.133.0 (2026-05-14)

Full Changelog: [v4.132.0...v4.133.0](https://github.com/team-telnyx/telnyx-python/compare/v4.132.0...v4.133.0)

### Features

* Add Speechmatics transcription engine to Call Control API ([dddb318](https://github.com/team-telnyx/telnyx-python/commit/dddb318e4706476fbe3452c920a1a95c8606abaa))

## 4.132.0 (2026-05-14)

Full Changelog: [v4.131.0...v4.132.0](https://github.com/team-telnyx/telnyx-python/compare/v4.131.0...v4.132.0)

### Features

* Document Conversation Relay ([5cb134d](https://github.com/team-telnyx/telnyx-python/commit/5cb134d1b06a6440f8c128297b93bdadcbfccac8))
* Fix Conversation Relay expected webhook ([277b46d](https://github.com/team-telnyx/telnyx-python/commit/277b46d020b58b756c7c773079dac0fa08febef3))

## 4.131.0 (2026-05-13)

Full Changelog: [v4.130.0...v4.131.0](https://github.com/team-telnyx/telnyx-python/compare/v4.130.0...v4.131.0)

### Features

* Document AI call status callback overrides ([87723f8](https://github.com/team-telnyx/telnyx-python/commit/87723f8a9160be89eaf88a209c621edb3fa27e0c))

## 4.130.0 (2026-05-11)

Full Changelog: [v4.129.0...v4.130.0](https://github.com/team-telnyx/telnyx-python/compare/v4.129.0...v4.130.0)

### Features

* **internal/types:** support eagerly validating pydantic iterators ([2d3d6ef](https://github.com/team-telnyx/telnyx-python/commit/2d3d6ef7b62ef00e12780ccce2830f035e64222c))

## 4.129.0 (2026-05-11)

Full Changelog: [v4.128.0...v4.129.0](https://github.com/team-telnyx/telnyx-python/compare/v4.128.0...v4.129.0)

### Features

* Document OpenAI responses conversation flow ([ea1550d](https://github.com/team-telnyx/telnyx-python/commit/ea1550d55e789043b8f67da65203f468fcaf8e13))

## 4.128.0 (2026-05-11)

Full Changelog: [v4.127.0...v4.128.0](https://github.com/team-telnyx/telnyx-python/compare/v4.127.0...v4.128.0)

### Features

* AI-2312: document currency and unit in /models pricing schema ([132d7d8](https://github.com/team-telnyx/telnyx-python/commit/132d7d8310b308408bdc1f7affc241a0722c824c))

## 4.127.0 (2026-05-11)

Full Changelog: [v4.126.0...v4.127.0](https://github.com/team-telnyx/telnyx-python/compare/v4.126.0...v4.127.0)

### Features

* Clean up OpenAI responses API docs ([9b429fa](https://github.com/team-telnyx/telnyx-python/commit/9b429fa699dc07660e0fb5d706e09ac550e454ab))

## 4.126.0 (2026-05-11)

Full Changelog: [v4.125.0...v4.126.0](https://github.com/team-telnyx/telnyx-python/compare/v4.125.0...v4.126.0)

### Features

* Fix OpenAI chat API reference links ([3b5021b](https://github.com/team-telnyx/telnyx-python/commit/3b5021b7b2bdb7636d138cd58430b097df6deeeb))

## 4.125.0 (2026-05-11)

Full Changelog: [v4.124.0...v4.125.0](https://github.com/team-telnyx/telnyx-python/compare/v4.124.0...v4.125.0)

### Features

* Responses endpoint ([4f46c79](https://github.com/team-telnyx/telnyx-python/commit/4f46c7970ef0d78935814d95e409a89bf78d7ad7))

## 4.124.0 (2026-05-08)

Full Changelog: [v4.123.1...v4.124.0](https://github.com/team-telnyx/telnyx-python/compare/v4.123.1...v4.124.0)

### Features

* AI-2294: document /ai/openai/models response and refresh LLM examples ([d03c497](https://github.com/team-telnyx/telnyx-python/commit/d03c497295687da246abea9c967acdcea4d0c4aa))

## 4.123.1 (2026-05-08)

Full Changelog: [v4.123.0...v4.123.1](https://github.com/team-telnyx/telnyx-python/compare/v4.123.0...v4.123.1)

### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([de93558](https://github.com/team-telnyx/telnyx-python/commit/de93558f5cebcbd39d8dcd3ca29df98dfd53d8da))

## 4.123.0 (2026-05-08)

Full Changelog: [v4.122.0...v4.123.0](https://github.com/team-telnyx/telnyx-python/compare/v4.122.0...v4.123.0)

### Features

* Add assistant external LLM forward metadata to OpenAPI ([8757bf7](https://github.com/team-telnyx/telnyx-python/commit/8757bf72210ec2f67eb8f9dc7b124cca3ee51690))
* Add Speechmatics provider to standalone STT spec ([a18a81b](https://github.com/team-telnyx/telnyx-python/commit/a18a81b0098201c177347fd2b7cc7571ae6e11e8))
* Add xAI and AssemblyAI transcription engines to call-control API docs ([e7162ca](https://github.com/team-telnyx/telnyx-python/commit/e7162ca12b956ce7192954979c5db09d9224c356))
* Add xAI and missing voice providers to Call Control API ([f1e4af5](https://github.com/team-telnyx/telnyx-python/commit/f1e4af5583447e52eecbd655f53d9aeee454c261))
* AI-2183: Document dynamic variable support for transcription keyterm ([74accfa](https://github.com/team-telnyx/telnyx-python/commit/74accfab45c00835cb24d2340980a568106ddfe7))
* AI-2289 add disable greeting interruption OpenAPI fields ([25cdd73](https://github.com/team-telnyx/telnyx-python/commit/25cdd73350350e122389b31c4bd723b789681171))
* Ai-assistant: update scheduled events api ([9b7be14](https://github.com/team-telnyx/telnyx-python/commit/9b7be14eba9ecd885941a4a1e23f869bd524e470))
* Ai-assistants: support pattern in canary deploy ([1353df1](https://github.com/team-telnyx/telnyx-python/commit/1353df199c7103b2793067a9a9b3ec3f56ecfd02))
* **api:** manual updates ([57f4244](https://github.com/team-telnyx/telnyx-python/commit/57f4244afe93f26e1f990675c8fe421b2fb45d64))
* **api:** manual updates ([a45c916](https://github.com/team-telnyx/telnyx-python/commit/a45c916a5760a204cf1de9c51cd7590152b7b566))
* **api:** manual updates ([f4f9625](https://github.com/team-telnyx/telnyx-python/commit/f4f9625aeb8a403a57163dcec431abe0a0b488cb))
* Assistant tool targets master ([18b768b](https://github.com/team-telnyx/telnyx-python/commit/18b768b4ee9a3a55c940b66583cf2b6efa7d5361))
* Correct external LLM forwarded metadata docs ([83f49da](https://github.com/team-telnyx/telnyx-python/commit/83f49dafcfcef5eaa50be7a66e113a4c80e4b602))
* Document assistant CRUD fields ([cfeda22](https://github.com/team-telnyx/telnyx-python/commit/cfeda22ea5cbd82ddf484b1c24bb34b1d2bcb806))
* Document Flux transcription language hints ([8806843](https://github.com/team-telnyx/telnyx-python/commit/88068433da34bf940f965d181175ee3ad79c2077))
* Document per-endpoint media encryption for call control ([29645d5](https://github.com/team-telnyx/telnyx-python/commit/29645d523cd683731603c61d0cf1af14bbe5357e))
* ENGDESK-51445: added profile ID fields to Whatsapp messages ([94a0b8c](https://github.com/team-telnyx/telnyx-python/commit/94a0b8c6c4053e048dc4516ae01e5902b217d27d))
* inference: expose chat completions and models under /ai/openai ([1021667](https://github.com/team-telnyx/telnyx-python/commit/102166782f0af2f08570c55a9407e436a264ef47))
* Mark 'from' as required on InviteToolConfig ([2e76296](https://github.com/team-telnyx/telnyx-python/commit/2e7629665addfeb690c522984804a2cf38289306))
* MSG-9000: document duplicate-vetting rejection on order brand external vetting ([eb04489](https://github.com/team-telnyx/telnyx-python/commit/eb044891f58a156db657b377075d55a278756d2b))
* Revert "fix: stainless ([#2371](https://github.com/team-telnyx/telnyx-python/issues/2371))" ([c3fd1fe](https://github.com/team-telnyx/telnyx-python/commit/c3fd1fe7f6d0192c5c2fd2558d0bfa4eab1532c2))
* TELAPPS-5725: Add deepfake detection params to call-scripting API docs ([ffe5768](https://github.com/team-telnyx/telnyx-python/commit/ffe5768681f7f883c7570061c026c727e4e25fc5))
* Update observability ([e82e1bc](https://github.com/team-telnyx/telnyx-python/commit/e82e1bc5e445eacd4b9e8fbb791df76e4acb4192))


### Bug Fixes

* **resources:** accept TeXML call params body ([640ef55](https://github.com/team-telnyx/telnyx-python/commit/640ef551079449da1d0b37f81c7368c37f5d85c7))
* revert stainless.yml changes from ad4f13c ([a87cc67](https://github.com/team-telnyx/telnyx-python/commit/a87cc67ed23669f7a5c984976a2fc5d8b2d40ca2))
* update UAC internal settings URI examples ([eb0ce1b](https://github.com/team-telnyx/telnyx-python/commit/eb0ce1b391f10dfc79b0980a16031dee7105c5ff))


### Reverts

* restore stainless.yml from before 964956c ([9cbd108](https://github.com/team-telnyx/telnyx-python/commit/9cbd108c5484d0387bf945fead829a2f21ca40fa))
* restore stainless.yml from before 9853597 ([1a62c7e](https://github.com/team-telnyx/telnyx-python/commit/1a62c7ed762ea51ce2304cf54fe5256b2263fff5))


### Chores

* **internal:** reformat pyproject.toml ([c783eb7](https://github.com/team-telnyx/telnyx-python/commit/c783eb7d32f8dc9b8b76ebf957c84a181850fd09))


### Documentation

* add UAC connection OpenAPI docs ([19eb8f1](https://github.com/team-telnyx/telnyx-python/commit/19eb8f1aa9c23335a4964519a7ef24db8a8212c8))
* update gather_using_ai transcription models ([11e14d6](https://github.com/team-telnyx/telnyx-python/commit/11e14d63339d30845914c051fe013cd4d17e88a6))

## 4.122.0 (2026-04-28)

Full Changelog: [v4.121.0...v4.122.0](https://github.com/team-telnyx/telnyx-python/compare/v4.121.0...v4.122.0)

### Features

* Fix CreateVerifyProfileRequest to match messaging-2fa schema ([b7cf6d2](https://github.com/team-telnyx/telnyx-python/commit/b7cf6d231849e9171d0b7cc06acd540301ca2a9a))

## 4.121.0 (2026-04-28)

Full Changelog: [v4.120.0...v4.121.0](https://github.com/team-telnyx/telnyx-python/compare/v4.120.0...v4.121.0)

### Features

* Update assistant transcription settings spec ([29d057f](https://github.com/team-telnyx/telnyx-python/commit/29d057f2d6a921aa0e6e9a64ceb8be7a4ca7cff4))

## 4.120.0 (2026-04-27)

Full Changelog: [v4.119.1...v4.120.0](https://github.com/team-telnyx/telnyx-python/compare/v4.119.1...v4.120.0)

### Features

* support setting headers via env ([4183f80](https://github.com/team-telnyx/telnyx-python/commit/4183f8022963b87125cb305254eaeb16301f96dd))

## 4.119.1 (2026-04-27)

Full Changelog: [v4.119.0...v4.119.1](https://github.com/team-telnyx/telnyx-python/compare/v4.119.0...v4.119.1)

### Bug Fixes

* use correct field name format for multipart file arrays ([28f1f94](https://github.com/team-telnyx/telnyx-python/commit/28f1f9420361be4f903a2796c2bfdd925545e84b))

## 4.119.0 (2026-04-24)

Full Changelog: [v4.118.0...v4.119.0](https://github.com/team-telnyx/telnyx-python/compare/v4.118.0...v4.119.0)

### Features

* Add call.hold and call.unhold webhook event documentation ([77aff88](https://github.com/team-telnyx/telnyx-python/commit/77aff884eb5102e5ed83397f4d3e62ba49eb5717))


### Documentation

* document dynamic variable support for voice_settings.voice ([d10475e](https://github.com/team-telnyx/telnyx-python/commit/d10475e9afc610f3a5c7aba4c7660acf7ebd8081))

## 4.118.0 (2026-04-23)

Full Changelog: [v4.117.0...v4.118.0](https://github.com/team-telnyx/telnyx-python/compare/v4.117.0...v4.118.0)

### Features

* Add xAI provider to standalone STT and TTS specs ([a82e445](https://github.com/team-telnyx/telnyx-python/commit/a82e4456ecd17b9fcd36c2ac794bc3839af517b4))


### Chores

* **internal:** more robust bootstrap script ([7071772](https://github.com/team-telnyx/telnyx-python/commit/7071772b854d997669c5e692057e969c1d017c7b))

## 4.117.0 (2026-04-22)

Full Changelog: [v4.116.0...v4.117.0](https://github.com/team-telnyx/telnyx-python/compare/v4.116.0...v4.117.0)

### Features

* MSG-6857: ([0075322](https://github.com/team-telnyx/telnyx-python/commit/0075322ba22bce4b8c7de269ab17185d82e835a8))

## 4.116.0 (2026-04-22)

Full Changelog: [v4.115.0...v4.116.0](https://github.com/team-telnyx/telnyx-python/compare/v4.115.0...v4.116.0)

### Features

* MSG-6841: add missing whatsapp api docs ([3c7d680](https://github.com/team-telnyx/telnyx-python/commit/3c7d6804e410b4bd36ee2083efbe5b6f61d9de39))

## 4.115.0 (2026-04-21)

Full Changelog: [v4.114.0...v4.115.0](https://github.com/team-telnyx/telnyx-python/compare/v4.114.0...v4.115.0)

### Features

* Add post_conversation_settings to AI Assistants API spec ([2c39b03](https://github.com/team-telnyx/telnyx-python/commit/2c39b03805e27202659f8c9c1edaa86e5dbb1573))

## 4.114.0 (2026-04-20)

Full Changelog: [v4.113.0...v4.114.0](https://github.com/team-telnyx/telnyx-python/compare/v4.113.0...v4.114.0)

### Features

* Add keyterm field to TranscriptionSettingsConfig ([61a6be9](https://github.com/team-telnyx/telnyx-python/commit/61a6be932105a04755f349e343b70bb06963d529))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([3536049](https://github.com/team-telnyx/telnyx-python/commit/3536049e8e7b42760fd33a962ad0eec146a6fe9d))

## 4.113.0 (2026-04-17)

Full Changelog: [v4.112.0...v4.113.0](https://github.com/team-telnyx/telnyx-python/compare/v4.112.0...v4.113.0)

### Features

* Add user_idle_reply_secs to TelephonySettings spec ([d3c21b4](https://github.com/team-telnyx/telnyx-python/commit/d3c21b472b54ea2799e204d63a31388aed11738a))

## 4.112.0 (2026-04-17)

Full Changelog: [v4.111.0...v4.112.0](https://github.com/team-telnyx/telnyx-python/compare/v4.111.0...v4.112.0)

### Features

* TELAPPS Provide description what params can be used for premium amd ([55f901d](https://github.com/team-telnyx/telnyx-python/commit/55f901d472c995ce062360543b98ef44c3913267))

## 4.111.0 (2026-04-16)

Full Changelog: [v4.110.0...v4.111.0](https://github.com/team-telnyx/telnyx-python/compare/v4.110.0...v4.111.0)

### Features

* Lower user_idle_timeout_secs minimum from 30s to 10s ([a0a79df](https://github.com/team-telnyx/telnyx-python/commit/a0a79dfcbe1de9ae8aafcc6bc5fbf4ee94eba4a1))


### Documentation

* add pagination params to conversation messages endpoint ([b9d0fae](https://github.com/team-telnyx/telnyx-python/commit/b9d0fae98af124d3c96e11eecb15d665de6a5ca9))

## 4.110.0 (2026-04-15)

Full Changelog: [v4.109.0...v4.110.0](https://github.com/team-telnyx/telnyx-python/compare/v4.109.0...v4.110.0)

### Features

* MSG-6868: document whitelisted_destinations as conditionally required ([ceaaffb](https://github.com/team-telnyx/telnyx-python/commit/ceaaffb4f9d116f57d5b5fe96554acb2c96eea08))

## 4.109.0 (2026-04-14)

Full Changelog: [v4.108.0...v4.109.0](https://github.com/team-telnyx/telnyx-python/compare/v4.108.0...v4.109.0)

### Features

* TELAPPS-5712: Add deepfake detection to call-control API spec ([a645d7e](https://github.com/team-telnyx/telnyx-python/commit/a645d7efa72197125e8bd7b71c2a70754be92d7e))

## 4.108.0 (2026-04-13)

Full Changelog: [v4.107.0...v4.108.0](https://github.com/team-telnyx/telnyx-python/compare/v4.107.0...v4.108.0)

### Features

* [TDA-6425] Fix session analysis API spec: relaxed date_time, remove status & completed_at ([93c33c4](https://github.com/team-telnyx/telnyx-python/commit/93c33c471f0221026f65e411ac34ca14b360175d))

## 4.107.0 (2026-04-13)

Full Changelog: [v4.106.0...v4.107.0](https://github.com/team-telnyx/telnyx-python/compare/v4.106.0...v4.107.0)

### Features

* **client:** allow enqueuing to websockets even when not connected ([5878b59](https://github.com/team-telnyx/telnyx-python/commit/5878b59e47bab464ad7d17e1b658a7869303642a))

## 4.106.0 (2026-04-13)

Full Changelog: [v4.105.1...v4.106.0](https://github.com/team-telnyx/telnyx-python/compare/v4.105.1...v4.106.0)

### Features

* Add webhook_urls, webhook_urls_method, webhook_retries_policies to Dial endpoint ([eaa792a](https://github.com/team-telnyx/telnyx-python/commit/eaa792a19419987b458d06abcf0174ba51e3d198))

## 4.105.1 (2026-04-12)

Full Changelog: [v4.105.0...v4.105.1](https://github.com/team-telnyx/telnyx-python/compare/v4.105.0...v4.105.1)

### Bug Fixes

* set additionalProperties=false on VoiceCloneUploadRequest to prevent codegen errors ([b4e8552](https://github.com/team-telnyx/telnyx-python/commit/b4e8552574460926bbcf98ba3cc0a328f9e5cedd))

## 4.105.0 (2026-04-11)

Full Changelog: [v4.104.1...v4.105.0](https://github.com/team-telnyx/telnyx-python/compare/v4.104.1...v4.105.0)

### Features

* **api:** manual updates ([143b22e](https://github.com/team-telnyx/telnyx-python/commit/143b22e1d3a24c65aab638bcb868f5dfcd940549))
* **client:** add event handler implementation for websockets ([137bcc6](https://github.com/team-telnyx/telnyx-python/commit/137bcc63bc09f9a01e958a463a42144d46726e65))
* **lib:** make ED25519 the default webhook verification ([5116ac8](https://github.com/team-telnyx/telnyx-python/commit/5116ac876f2a99d3664d59d2ee9bf50a0c9c3387))


### Bug Fixes

* resolve pyright type error in text_to_speech event handler ([e209866](https://github.com/team-telnyx/telnyx-python/commit/e209866009201d11ac5aabaf49bfe66cb67ec885))


### Documentation

* improve examples ([4e53d34](https://github.com/team-telnyx/telnyx-python/commit/4e53d34555a18b433d5f5eff075057387fd5ecb7))

## 4.104.1 (2026-04-10)

Full Changelog: [v4.104.0...v4.104.1](https://github.com/team-telnyx/telnyx-python/compare/v4.104.0...v4.104.1)

### Bug Fixes

* ensure file data are only sent as 1 parameter ([f0cb6ac](https://github.com/team-telnyx/telnyx-python/commit/f0cb6ac811a97399d137852b207e3b18822297b1))

## 4.104.0 (2026-04-10)

Full Changelog: [v4.103.0...v4.104.0](https://github.com/team-telnyx/telnyx-python/compare/v4.103.0...v4.104.0)

### Features

* **api:** Merge pull request [#46](https://github.com/team-telnyx/telnyx-python/issues/46) from stainless-sdks/FixModelRecommendation ([911071c](https://github.com/team-telnyx/telnyx-python/commit/911071c8cf4c85514d0730be91dbb93d65a61ebf))

## 4.103.0 (2026-04-10)

Full Changelog: [v4.102.0...v4.103.0](https://github.com/team-telnyx/telnyx-python/compare/v4.102.0...v4.103.0)

### Features

* MSG-6846: add GET /profile/photo docs for whatsapp API ([47e8f01](https://github.com/team-telnyx/telnyx-python/commit/47e8f018531b5c4a702e5185e144df004fe7cfab))


### Reverts

* restore stainless.yml to pre-6a6df5b state ([4f9838b](https://github.com/team-telnyx/telnyx-python/commit/4f9838bfc30b134a842f4313ea784121821b31c7))

## 4.102.0 (2026-04-09)

Full Changelog: [v4.101.0...v4.102.0](https://github.com/team-telnyx/telnyx-python/compare/v4.101.0...v4.102.0)

### Features

* add shared CallAssistantRequest schema for call-control assistant object ([b24aecf](https://github.com/team-telnyx/telnyx-python/commit/b24aecff912822fadd885d4be7319b2817d48a95))

## 4.101.0 (2026-04-09)

Full Changelog: [v4.100.0...v4.101.0](https://github.com/team-telnyx/telnyx-python/compare/v4.100.0...v4.101.0)

### Features

* **api:** Merge pull request [#44](https://github.com/team-telnyx/telnyx-python/issues/44) from stainless-sdks/fix-NameNotAllowed ([a19231b](https://github.com/team-telnyx/telnyx-python/commit/a19231bd8d47f96fbf45dde2b87adf588522a3e7))

## 4.100.0 (2026-04-09)

Full Changelog: [v4.99.0...v4.100.0](https://github.com/team-telnyx/telnyx-python/compare/v4.99.0...v4.100.0)

### Features

* **client:** support reconnection in websockets ([4f8ca17](https://github.com/team-telnyx/telnyx-python/commit/4f8ca177181fe2c0747bdd045356f7841b70690f))


### Reverts

* revert stainless.yml changes from 9c5e8d8 ([9930faa](https://github.com/team-telnyx/telnyx-python/commit/9930faa7d2d54bb6b50e100c6fbfb96bea0a1043))


### Documentation

* update voice clone schemas to match Ultra/model_id implementation ([f370dde](https://github.com/team-telnyx/telnyx-python/commit/f370dde4582bfe7714d7efc8be3571028a8cf7aa))

## 4.99.0 (2026-04-08)

Full Changelog: [v4.98.0...v4.99.0](https://github.com/team-telnyx/telnyx-python/compare/v4.98.0...v4.99.0)

### Features

* TELAPPS-5707: Add privacy parameter to Call Control dial and transfer ([994a4ae](https://github.com/team-telnyx/telnyx-python/commit/994a4ae45ea23d56e53d9b63c0900ff194579b81))


### Reverts

* revert stainless.yml changes from pronunciation dictionaries commit ([62f4c82](https://github.com/team-telnyx/telnyx-python/commit/62f4c82b7231098bac5254a4a4ae05ec0c5550a4))

## 4.98.0 (2026-04-08)

Full Changelog: [v4.97.0...v4.98.0](https://github.com/team-telnyx/telnyx-python/compare/v4.97.0...v4.98.0)

### Features

* TELAPPS-5689: Pronunciation dictionaries API docs ([eb1bebf](https://github.com/team-telnyx/telnyx-python/commit/eb1bebfd40a114d54025e1b151f28d55de88ffa6))

## 4.97.0 (2026-04-08)

Full Changelog: [v4.96.0...v4.97.0](https://github.com/team-telnyx/telnyx-python/compare/v4.96.0...v4.97.0)

### Features

* Add ai_calls endpoint documentation to OpenAPI spec ([586c445](https://github.com/team-telnyx/telnyx-python/commit/586c44557cec717765f9aff0e7f67b4f81a2d50a))
* Add oneOf constraint for Url/Texml mutual exclusivity in InitiateCallRequest ([a444d3a](https://github.com/team-telnyx/telnyx-python/commit/a444d3a66987f8d6625e3dbce7ab69625e21e7ae))
* **api:** Merge pull request [#39](https://github.com/team-telnyx/telnyx-python/issues/39) from stainless-sdks/revert-a988c49-stainless-changes ([75ee85b](https://github.com/team-telnyx/telnyx-python/commit/75ee85b1f03acee3d5a759ab13503c8ac5da729b))
* **client:** support sending raw data over websockets ([f475022](https://github.com/team-telnyx/telnyx-python/commit/f4750222c54658dfa0e2a43bc54758e7128f6275))
* CW-3815 fix PATCH /wirelss_blocklists/{id} endpoint ([5b7eb9f](https://github.com/team-telnyx/telnyx-python/commit/5b7eb9f2335152f2ba68a4a06c578e95761b6c41))


### Reverts

* restore stainless.yml SDK generation fixes ([75ee85b](https://github.com/team-telnyx/telnyx-python/commit/75ee85b1f03acee3d5a759ab13503c8ac5da729b))

## 4.96.0 (2026-04-07)

Full Changelog: [v4.95.0...v4.96.0](https://github.com/team-telnyx/telnyx-python/compare/v4.95.0...v4.96.0)

### Features

* AI-2180: Add message_template to SendMessageTool schema ([7e21d03](https://github.com/team-telnyx/telnyx-python/commit/7e21d03c66deab58fdad063a0f9b2b14805576d2))

## 4.95.0 (2026-04-07)

Full Changelog: [v4.94.1...v4.95.0](https://github.com/team-telnyx/telnyx-python/compare/v4.94.1...v4.95.0)

### Features

* add enabled boolean to recording_settings [AI-2178] ([0c7505a](https://github.com/team-telnyx/telnyx-python/commit/0c7505a6f76751c5a88fa715624f554be6325a80))

## 4.94.1 (2026-04-07)

Full Changelog: [v4.94.0...v4.94.1](https://github.com/team-telnyx/telnyx-python/compare/v4.94.0...v4.94.1)

### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([acc1ed8](https://github.com/team-telnyx/telnyx-python/commit/acc1ed8681f91c7f601916c297dc2fa0a4b59617))

## 4.94.0 (2026-04-07)

Full Changelog: [v4.93.0...v4.94.0](https://github.com/team-telnyx/telnyx-python/compare/v4.93.0...v4.94.0)

### Features

* **api:** manual updates ([16342a1](https://github.com/team-telnyx/telnyx-python/commit/16342a1b12cb9b1bd14b03cb54023defcf105a96))

## 4.93.0 (2026-04-07)

Full Changelog: [v4.92.0...v4.93.0](https://github.com/team-telnyx/telnyx-python/compare/v4.92.0...v4.93.0)

### Features

* MSG-6666: Add template and text properties to WhatsApp send message schema ([313ba3d](https://github.com/team-telnyx/telnyx-python/commit/313ba3d602d43079854e8b8dc8ee8a68c8cf5c47))

## 4.92.0 (2026-04-07)

Full Changelog: [v4.91.0...v4.92.0](https://github.com/team-telnyx/telnyx-python/compare/v4.91.0...v4.92.0)

### Features

* Assistants: add observability ([0782eea](https://github.com/team-telnyx/telnyx-python/commit/0782eeabd629a5178d4db6ace324398c5b9b6094))

## 4.91.0 (2026-04-07)

Full Changelog: [v4.90.0...v4.91.0](https://github.com/team-telnyx/telnyx-python/compare/v4.90.0...v4.91.0)

### Features

* MSG-6673: Add WhatsApp verification endpoint and profile settings ([e873736](https://github.com/team-telnyx/telnyx-python/commit/e8737361ace9db26d4f9e89ed79ceada7c89caa8))

## 4.90.0 (2026-03-31)

Full Changelog: [v4.89.0...v4.90.0](https://github.com/team-telnyx/telnyx-python/compare/v4.89.0...v4.90.0)

### Features

* **lib:** add ED25519 webhook signature verification ([18be54b](https://github.com/team-telnyx/telnyx-python/commit/18be54bff12109ba79b6ba2a80a881fdfaa523f0))

## 4.89.0 (2026-03-30)

Full Changelog: [v4.88.1...v4.89.0](https://github.com/team-telnyx/telnyx-python/compare/v4.88.1...v4.89.0)

### Features

* **lib:** add Speech-to-Text WebSocket streaming support ([b7e059a](https://github.com/team-telnyx/telnyx-python/commit/b7e059ab7d86a982f8773a420867f827fde2ca51))


### Bug Fixes

* resolve pyright strict mode type errors ([3283d71](https://github.com/team-telnyx/telnyx-python/commit/3283d71d81d515147e7c2b96acf541f38ae34f9c))
* resolve ruff import sorting errors ([f210455](https://github.com/team-telnyx/telnyx-python/commit/f2104551e00dedd2db3bab6596e58591efd899ef))

## 4.88.1 (2026-03-28)

Full Changelog: [v4.88.0...v4.88.1](https://github.com/team-telnyx/telnyx-python/compare/v4.88.0...v4.88.1)

### Bug Fixes

* **python:** add edition python.2025-11-20 for OIDC support ([018532e](https://github.com/team-telnyx/telnyx-python/commit/018532e7217cd1a3b03530b76d84a9f9d2302528))


### Chores

* sync repo ([a70b9c2](https://github.com/team-telnyx/telnyx-python/commit/a70b9c2922e4196876a3c68057e461c63cc44f5f))
