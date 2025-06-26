# [My Mermaid Practice](../README.md#my-mermaid--practice)

Technologia~


### **\<References>**

- [https://mermaid-js.github.io/](https://mermaid-js.github.io/)
- [Mermaid Live Editor](https://mermaid.live/)


### **\<List>**

- [Initial Practice (2025.06.25)](#initial-practice-20250625)


## [Initial Practice (2025.06.25)](#list)

- Practice drawing various charts with *Mermaid* : Mindmap, Flowchart, and ERDiagram

### Mindmap : Ohtani's Mandalart
```mermaid
mindmap
  root((8구단 드래프트 1순위))
    (몸 만들기)
      몸관리
      영양제 먹기
      FSQ 90kg
      RSQ 130kg
      식사 저녁6숟갈 아침3숟갈
      가동역
      스테미너
      유연성
    (제구)
      인스텝 개선
      몸통 강화
      축 흔들지 않기
      불안정 없애기
      멘탈을 컨트롤
      몸을 열지 않기
      하체 강화
      릴리즈 포인트 안정
    (구위)
      각도를 만든다
      위에서부터 공을 던진다
      손목 강화
      하반식 주도
      가동력
      회전수 증가
      볼을 앞에서 릴리즈
      힘 모으기
    (스피드 160km/h)
      축을 돌리기
      하체 강화
      체중 증가
      어깨주변 강화
      피칭 늘리기
      라이너 캐치볼
      가동력
      몸통 강화
    (변화구)
      카운트볼 늘리기
      포크볼 완성
      슬라이더 구위
      좌타자 결정구
      거리를 상상하기
      스트라이크 볼을 던질 때 제구
      직구와 같은 폼으로 던지기
      늦게 낙차가 있는 커브
    (운)
      인사하기
      쓰레기 줍기
      부실 청소
      심판을 대하는 태도
      책읽기
      응원받는 사람
      긍정적 사고
      물건을 소중히 쓰자
    (인간성)
      감성
      사랑받는 사람
      계획성
      감사
      지속력
      신뢰받는 사람
      예의
      배려
    (멘탈)
      뚜렷한 목표·목적
      일희일비하지 않기
      머리는 차갑게 심장은 뜨겁게
      분위기에 휩쓸리지 않기
      동료를 배려하는 마음
      승리에 대한 집념
      마음의 파도를 안 만들기
      핀치에 강하게
```

### Flowchart : Doomed to Open a Chicken Shop
```mermaid
flowchart TD
  A[진로 고민] --> B{어떤 길을 선택할까?}
  B --> C1[대기업 취업]
  B --> C2[공무원 준비]
  B --> C3[창업 도전]
  B --> C4[해외 유학]
  C1 --> D
  C2 --> D
  C3 --> D
  C4 --> D
  D[결국 치킨집 사장]
```

### ERDiagram : Dad and Boy
```mermaid
erDiagram
  DAD {
    string name
    int patienceLevel
  }
  BOY {
    string name
    int energyLevel
  }
  TOY {
    string type
    bool broken
  }
  SNACK {
    string flavor
    int sugarContent
  }
  DAD ||--o{ TOY : "fixes"
  BOY ||--o{ TOY : "breaks"
  DAD ||--o{ SNACK : "hides"
  BOY ||--o{ SNACK : "finds"
  DAD ||--|| BOY : "raises"
```
