
# PROJECT SONGGOLMAE
> 부산대학교 제3회 창의융합SW해커톤

## Investment Simulation Platform (phase-1)
증권API,크롤링으로 얻은 주가데이터를 투자전략에 따라 시뮬레이션 해 봄으로써 투자에 도움을 줍니다.

### Details
1. 사용자가 매수, 매도의 기준을 직접 설정합니다.
- 매출액, 영업이익, 주가, 시가총액, PER, PBR, ROE, 현금흐름, 부채 비율 등의 지표가 있습니다. 
- 사용자가 주도적으로 매수, 매도 기준을 설정합니다. 

2. 백테스팅 서비스를 제공합니다. 
- 특정 기간을 설정하고, 사용자가 선택한 전략대로 과거 시뮬레이션을 진행합니다. 
- 과거 주가 데이터를 활용하여 불확실성을 줄이고, 자신만의 투자 전략을 수립합니다. 
- 실제처럼 실행하고 모든 결과를 기록해 분석합니다. 
- 전략의 성과를 평가합니다. 

3. 플랫폼 자체 커뮤니티로 투자자간 정보 공유 서비스를 제공합니다.
- 자신의 전략에 대한 다른 사람의 의견을 듣기 위해 백테스팅 데이터를 커뮤니티에 공유할 수 있습니다. 
- 커뮤니티에서 의견을 주고받으며 투자에 관한 다양한 지식을 쌓을 수 있습니다. 또한, 전략을 평가받고 부족한 것이나 잘못된 것을 고칠 수 있습니다.
- 백테스팅으로 구한 수익률 데이터를, 다양한 측면을 반영한 수치로 분석하여 나에게 적합한 전략인지 아닌지 판가름 해줍니다. 

## Tech/framework used
- Framework : Django3.0, Django-Rest-Framework
- Language : python3.8(32/64), javascript
- OS : Ubuntu 18.0.4
- DB : MongoDB Atlas
- Cloud : AWS-EC2


[![NPM Version][npm-image]][npm-url]
[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

## Working - On

frontend - next.js npm url: http://afa5523565ae.ngrok.io

backend - django-rest-framework ngrok url: http://fa3849b69ce8.ngrok.io/apis/

backend - django-admin page url: http://fa3849b69ce8.ngrok.io/admin

mongodb - atlas database: https://cloud.mongodb.com/v2/5f376e368a7cea3dc026163b#clusters

## Log-in page

![intro page3-01](https://user-images.githubusercontent.com/37919421/90789133-7f84a400-e341-11ea-8ed5-eb9b56e4d85c.png)

## Community page
![community main0820-01](https://user-images.githubusercontent.com/37919421/90789500-f5890b00-e341-11ea-867f-338e7f82565c.png)

## My page
![my page0817-01](https://user-images.githubusercontent.com/37919421/90789593-0afe3500-e342-11ea-8d6f-da898ca1508a.png)

## Installation

OS X & Linux:

```sh
npm install my-crazy-module --save
```

Windows:

```sh
edit autoexec.bat
```

## Usage example

A few motivating and useful examples of how your product can be used. Spice this up with code blocks and potentially more screenshots.

_For more examples and usage, please refer to the [Wiki][wiki]._

## Development setup

Describe how to install all development dependencies and how to run an automated test-suite of some kind. Potentially do this for multiple platforms.

```sh
make install
npm test
```

## Release History

* 0.2.1
    * CHANGE: Update docs (module code remains unchanged)
* 0.2.0
    * CHANGE: Remove `setDefaultXYZ()`
    * ADD: Add `init()`
* 0.1.1
    * FIX: Crash when calling `baz()` (Thanks @GenerousContributorName!)
* 0.1.0
    * The first proper release
    * CHANGE: Rename `foo()` to `bar()`
* 0.0.1
    * Work in progress

## Meta

Your Name – [@YourTwitter](https://twitter.com/dbader_org) – YourEmail@example.com

Distributed under the XYZ license. See ``LICENSE`` for more information.

[https://github.com/yourname/github-link](https://github.com/dbader/)

## Contributing

1. Fork it (<https://github.com/yourname/yourproject/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
