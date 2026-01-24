# Hypothalamus Engine (시상하부 엔진)

**Version**: 1.0.0-alpha  
**Status**: 소프트웨어 벤치마킹 단계 (물리적 하드웨어 테스트 미완)  
**License**: MIT License  
**Author**: GNJz (Qquarts)

---

## ⚠️ 중요 안내

**현재 상태**: 본 엔진은 소프트웨어 시뮬레이션 및 벤치마킹 단계에 있습니다.  
**물리적 하드웨어 테스트는 아직 완료되지 않았으며**, 실제 산업 환경에 적용하기 전에 추가 검증이 필요합니다.

본 프로젝트는 **계속 발전하는 구조**이며, 테스트 과정과 계획된 업그레이드를 통해 확장되어 갑니다.

---

## 📋 개요

**Hypothalamus Engine**은 산업용 동기 부여 및 에너지 관리 시스템을 목표로 하는 소프트웨어 엔진입니다. 생물학적 시상하부의 기능을 모사하여 에너지 관리, 욕구 시스템, 보상 시스템, 생체 리듬 조절 등의 기능을 제공합니다.

### 핵심 기능

- ✅ **에너지 관리**: 활동 시 소모, 수면 시 회복
- ✅ **욕구 시스템**: 수면, 탐험, 학습, 사회적 상호작용 등
- ✅ **보상 시스템**: 도파민 기반 동기 부여
- ✅ **각성 수준 계산**: 에너지 × (1 - 지루함) × (1 + 도파민 보정)
- ✅ **생체 리듬**: 수면-각성 주기 조절

---

## 🎯 예상 산업 활용 분야

**참고**: 아래는 본 엔진의 잠재적 활용 분야이며, 실제 적용을 위해서는 추가 검증이 필요합니다.

### 1. 로봇 에너지 관리 시스템 (예상)
- 로봇의 에너지 상태 모니터링
- 에너지 부족 시 자동 휴식 모드 전환
- 작업 우선순위 조절

### 2. 게임 AI 동기 시스템 (예상)
- NPC의 동기 부여 시스템
- 보상 기반 학습 강화
- 개성 있는 캐릭터 행동 패턴

### 3. 자율 시스템 관리 (예상)
- 시스템 부하 관리
- 자동 휴식 및 복구
- 동적 리소스 할당

---

## 🚀 빠른 시작

### 설치

```bash
pip install -r requirements.txt
```

### 기본 사용법

```python
from hypothalamus import HypothalamusEngine, HypothalamusConfig

# 설정
config = HypothalamusConfig(
    energy_decay=0.005,      # 에너지 감쇠율
    curiosity_weight=1.2     # 호기심 가중치
)

# 엔진 초기화
engine = HypothalamusEngine(config)

# 상태 업데이트
engine.tick(action_type='think', stimulus_level=0.3)

# 현재 욕구 확인
drive = engine.get_current_drive()
print(f"현재 욕구: {drive.drive_type.value}, 긴급도: {drive.urgency:.2f}")

# 보상 수신
engine.receive_reward('success', intensity=0.8)

# 각성 수준 확인
arousal = engine.get_arousal_level()
print(f"각성 수준: {arousal:.2f}")
```

---

## 📐 핵심 수식

### 1. 에너지 감쇠 (활동 시)

```
E(t) = E_0 - λ·t·(1 + multiplier)
```

- `E_0`: 초기 에너지 (0~1)
- `λ`: energy_decay (기본값 0.005)
- `multiplier`: 활동 유형에 따른 배수 (think: 2.0, learn/chat: 1.0)

### 2. 에너지 회복 (수면 시)

```
E(t) = E_0 + μ·t
```

- `μ`: energy_recovery (기본값 0.02)

### 3. 지루함 증가

```
B(t) = B_0 + α·t·(1-S)  (자극 없을 때)
B(t) = B_0 - β·S·t      (자극 있을 때)
```

- `B_0`: 초기 지루함 (0~1)
- `α`: boredom_increase (기본값 0.01)
- `β`: boredom_decrease (기본값 0.05)
- `S`: stimulus_level (0~1)

### 4. 도파민 반응 (보상 수신 시)

```
D = D_base + β·R·(1-D)
```

- `D_base`: 현재 도파민 (0~1)
- `β`: dopamine_boost (기본값 0.15)
- `R`: reward_intensity (0~1)
- 현재 도파민이 낮을수록 더 큰 효과

### 5. 욕구 우선순위

```
P = w_E·(1-E) + w_B·B + w_S·S + w_L·L + w_C·C
```

- `w_E`: energy_weight (기본값 1.5)
- `w_B`: boredom_weight (기본값 1.0)
- `w_S`: stress_weight (기본값 1.2)
- `w_L`: loneliness_weight (기본값 0.8)
- `w_C`: curiosity_weight (기본값 0.9)
- `E`: energy (0~1)
- `B`: boredom (0~1)
- `S`: stress (0~1)
- `L`: loneliness (0~1)
- `C`: curiosity (0~1)

### 6. 각성 수준

```
A = E · (1 - B) · (1 + (D - 0.5) · 0.5)
```

- `E`: energy (0~1)
- `B`: boredom (0~1)
- `D`: dopamine (0~1)
- 범위: 0.0 (최저 각성) ~ 1.0 (최고 각성)

---

## ⚙️ 설정 (HypothalamusConfig)

### 주요 파라미터

| 파라미터 | 기본값 | 설명 |
|---------|--------|------|
| `sleep_threshold` | 0.2 | 수면 필요 임계값 (에너지) |
| `critical_threshold` | 0.1 | 강제 수면 임계값 (에너지) |
| `boredom_threshold` | 0.7 | 탐험 필요 임계값 (지루함) |
| `stress_threshold` | 0.8 | 휴식 필요 임계값 (스트레스) |
| `energy_decay` | 0.005 | 틱당 에너지 감소 |
| `energy_recovery` | 0.02 | 수면 시 에너지 회복 |
| `dopamine_boost` | 0.15 | 보상 시 도파민 증가율 |
| `energy_weight` | 1.5 | 에너지 가중치 |
| `boredom_weight` | 1.0 | 지루함 가중치 |
| `curiosity_weight` | 0.9 | 호기심 가중치 |

### 설정 예제

```python
# 호기심 많은 성격
curious_config = HypothalamusConfig(
    curiosity_weight=2.0,
    energy_decay=0.003  # 에너지 소모 느림
)

# 활동적인 성격
active_config = HypothalamusConfig(
    energy_decay=0.01,  # 에너지 소모 빠름
    boredom_weight=1.5  # 지루함에 민감
)
```

---

## 📊 API 문서

### HypothalamusEngine

#### `tick(action_type: str, stimulus_level: float)`

매 틱마다 내부 상태 업데이트

**Args:**
- `action_type`: 현재 행동 ('think', 'learn', 'chat', 'sleep', 'idle')
- `stimulus_level`: 자극 수준 (0~1)

#### `get_current_drive() -> DriveSignal`

현재 가장 시급한 욕구 반환

**Returns:**
- `DriveSignal`: 욕구 유형, 긴급도, 메시지, 권장 행동

#### `receive_reward(reward_type: str, intensity: float) -> float`

보상 수신 → 도파민 분비

**Args:**
- `reward_type`: 보상 유형 ('success', 'praise', 'learn', 'social', 'achievement')
- `intensity`: 보상 강도 (0~1)

**Returns:**
- 도파민 증가량

#### `get_arousal_level() -> float`

각성 수준 계산 및 반환

**Returns:**
- 각성 수준 (0.0 ~ 1.0)

#### `get_energy_state() -> Dict[str, float]`

에너지 상태 노출 인터페이스

**Returns:**
- 에너지 관련 상태 딕셔너리

#### `sleep_cycle(cycles: int) -> str`

수면 사이클 실행

**Args:**
- `cycles`: 수면 사이클 수

**Returns:**
- 수면 완료 메시지

#### `get_state() -> Dict[str, Any]`

전체 상태 반환

#### `get_stats() -> Dict[str, Any]`

통계 반환

---

## 🧪 예제

### 예제 1: 기본 사용

```python
from hypothalamus import HypothalamusEngine, HypothalamusConfig

config = HypothalamusConfig()
engine = HypothalamusEngine(config)

# 활동 시뮬레이션
for i in range(10):
    engine.tick(action_type='think', stimulus_level=0.3)

# 현재 욕구 확인
drive = engine.get_current_drive()
print(f"욕구: {drive.drive_type.value}, 긴급도: {drive.urgency:.2f}")
```

### 예제 2: 보상 시스템

```python
# 보상 수신
dopamine_gain = engine.receive_reward('praise', intensity=0.8)
print(f"도파민 증가: {dopamine_gain:.3f}")

# 각성 수준 확인
arousal = engine.get_arousal_level()
print(f"각성 수준: {arousal:.2f}")
```

자세한 예제는 `examples/` 폴더를 참고하세요.

---

## ⚠️ 현재 제한사항 및 주의사항

### 현재 상태
- **소프트웨어 벤치마킹 단계**: 물리적 하드웨어 테스트는 아직 완료되지 않았습니다.
- **시뮬레이션 환경**: 실제 시스템과의 통합 테스트는 미완성 상태입니다.
- **성능 검증**: 대규모 실시간 환경에서의 성능 검증이 필요합니다.

### 기능적 제한사항
- 본 모듈은 **동기 부여 및 에너지 관리 계층**이며, 단독 의사결정 시스템은 아닙니다.
- 대규모 경로 계획(Path Planning) 또는 복잡한 의사결정 기능은 포함하지 않습니다.
- 실제 생물학적 시상하부의 모든 기능을 완전히 모사하지는 않습니다.

### 향후 계획
- 물리적 하드웨어 통합 테스트
- 실시간 환경 성능 검증
- 대규모 데이터셋 벤치마킹

---

## ⏱️ 권장 시간 스케일

- 제어 주기(dt): 0.1초 ~ 1초
- 상태 업데이트 주기: 시스템 틱 주기와 동일
- 수면 사이클: 10~20 사이클 권장

---

## 🎛️ Gain 튜닝 가이드

- `energy_decay` ↑ : 빠른 에너지 소모 (활동적인 성격)
- `curiosity_weight` ↑ : 호기심 많은 성격
- `boredom_weight` ↑ : 지루함에 민감한 성격
- `dopamine_boost` ↑ : 보상에 더 강하게 반응
- `energy_recovery` ↑ : 빠른 에너지 회복

---

## 🔒 안전성 고려사항

**중요**: 본 모듈은 소프트웨어 시뮬레이션 단계이며, 실제 안전-중요(safety-critical) 시스템에 적용하기 전에 철저한 검증이 필요합니다.

- 본 모듈은 동기 부여 및 에너지 관리를 위한 것이나, 실제 안정성 검증은 아직 완료되지 않았습니다.
- 실제 산업 환경 적용 시 추가 안전성 검증 및 인증이 필요할 수 있습니다.

---

## 🔮 향후 계획 및 로드맵

본 프로젝트는 계속 발전하는 구조이며, 다음 단계를 계획하고 있습니다:

### v1.1 (계획 중)
- 다중 에이전트 환경 지원
- 외부 에너지 공급 시스템 연동
- 고급 보상 시스템

### v1.2+ (장기 계획)
- 물리적 하드웨어 통합 테스트
- 실시간 C/C++ 바인딩
- 대규모 실시간 환경 성능 검증

**참고**: 로드맵은 테스트 결과와 피드백에 따라 변경될 수 있습니다.

---

## 📚 참고 논문

- Swanson (2000): Hypothalamus structure and function
- Berridge & Kringelbach (2015): Affective neuroscience of pleasure
- Saper et al. (2005): Hypothalamic regulation of sleep and circadian rhythms

---

## 📄 라이선스

MIT License

---

## 👤 작성자

GNJz (Qquarts)

---

## 🔗 PHAM 블록체인 서명

이 Hypothalamus Engine은 **PHAM (Proof of Authorship & Merit) 블록체인 시스템**으로 서명되어 있습니다.

### 블록체인 정보

- **블록체인 체인 파일**: `blockchain/pham_chain_*.json`
- **4-Signal Scoring**: Byte(25%) + Text(35%) + AST(30%) + Exec(10%)
- **IPFS 저장**: 모든 코드 버전이 IPFS에 영구 보존됨
- **자세한 내용**: `BLOCKCHAIN_INFO.md` 참조

### 블록체인 기반 기여도 시스템

이 엔진은 **오픈소스**로 제공되며, 자유롭게 연구, 재사용, 확장이 가능합니다.

**⚠️ 중요**: 코드 재사용 시 로열티를 요구하지 않습니다. 사용 제한도 없습니다.

**하지만**, 이 코드를 사용하여 **수익이 발생하는 시점부터**는 블록체인 기반 기여도 시스템이 작동합니다:

- **코드 기여도**와 **제품 기여도**(상용화, 홍보, 마케팅, 판매 등)가 모두 블록체인에 기록되어 합산됩니다
- 모든 기여 활동이 블록체인에 기록되어 투명하게 관리됩니다
- 블록체인으로 계산된 기여도에 따라 수익이 자동으로 분배됩니다

**🔄 업그레이드 가능한 구조**: 이 블록체인 기반 기여도 시스템 자체도 계속 업그레이드되어가는 구조입니다. 현재는 초기 설계 단계이며, 실제 상용화가 이루어지고 경험이 쌓이면서 시스템이 발전하고 개선될 예정입니다.

**⚠️ GNJz의 기여도 원칙 (블록체인 기반)**: 최초 코드 작성자 GNJz (Qquarts)는 자신의 기여도가 총 기여도 중 **6%를 넘지 않도록 제한합니다**. 이것은 "로열티를 6%로 받겠다"는 요구가 아니라, **블록체인으로 검증 가능한 기여도 상한선**입니다. 코드 재사용 시 로열티를 요구하지 않으며, 수익 발생 시 블록체인으로 계산된 기여도에 따라 수익이 분배됩니다. 모든 기여도 계산은 블록체인에 기록되어 누구나 검증할 수 있습니다.

### 블록체인 체인 확인

```bash
# 블록체인 체인 파일 확인
cat blockchain/pham_chain_hypothalamus_engine.json | jq '.'

# 기여도 통계 확인
python3 ../cookiie_brain/blockchain/pham_sign_v4.py --stats blockchain/pham_chain_hypothalamus_engine.json
```

---

**Made in GNJz** 🧠

