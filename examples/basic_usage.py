"""
Hypothalamus Engine Basic Usage Example
시상하부 엔진 기본 사용 예제

Author: GNJz (Qquarts)
Version: 1.0.0-alpha
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from hypothalamus import HypothalamusEngine, HypothalamusConfig, DriveType


def main():
    """기본 사용 예제"""
    print("=" * 60)
    print("🧠 Hypothalamus Engine - Basic Usage Example")
    print("=" * 60)
    
    # 1. 엔진 초기화
    print("\n[1] 엔진 초기화")
    print("-" * 40)
    config = HypothalamusConfig(
        energy_decay=0.005,
        curiosity_weight=1.2  # 호기심 가중치 증가
    )
    engine = HypothalamusEngine(config)
    
    state = engine.get_state()
    print(f"초기 에너지: {state['internal_state']['energy']:.2f}")
    print(f"초기 도파민: {state['internal_state']['dopamine']:.2f}")
    print(f"초기 지루함: {state['internal_state']['boredom']:.2f}")
    
    # 2. 활동 시뮬레이션
    print("\n[2] 활동 시뮬레이션 (10틱)")
    print("-" * 40)
    for i in range(10):
        engine.tick(action_type='think', stimulus_level=0.3)
    
    state = engine.get_state()
    print(f"에너지: {state['internal_state']['energy']:.2f} (감소)")
    print(f"지루함: {state['internal_state']['boredom']:.2f}")
    
    # 3. 현재 욕구 확인
    print("\n[3] 현재 욕구 확인")
    print("-" * 40)
    drive = engine.get_current_drive()
    print(f"욕구 유형: {drive.drive_type.value}")
    print(f"긴급도: {drive.urgency:.2f}")
    print(f"메시지: {drive.message}")
    print(f"권장 행동: {drive.action_suggestion}")
    
    # 4. 보상 수신
    print("\n[4] 보상 수신")
    print("-" * 40)
    old_dopamine = engine.state.dopamine
    dopamine_gain = engine.receive_reward('praise', intensity=0.8)
    print(f"도파민: {old_dopamine:.2f} → {engine.state.dopamine:.2f} (+{dopamine_gain:.3f})")
    
    # 5. 각성 수준 확인
    print("\n[5] 각성 수준 확인")
    print("-" * 40)
    arousal = engine.get_arousal_level()
    print(f"각성 수준: {arousal:.2f}")
    
    energy_state = engine.get_energy_state()
    print(f"에너지 상태:")
    print(f"  - 에너지: {energy_state['energy']:.2f}")
    print(f"  - 각성 수준: {energy_state['arousal_level']:.2f}")
    print(f"  - 수면 필요: {energy_state['is_sleep_needed']}")
    print(f"  - 위급 상태: {energy_state['is_critical']}")
    
    # 6. 지루함 시뮬레이션
    print("\n[6] 지루함 시뮬레이션 (30틱 대기)")
    print("-" * 40)
    for i in range(30):
        engine.tick(action_type='idle', stimulus_level=0.0)
    
    state = engine.get_state()
    print(f"지루함: {state['internal_state']['boredom']:.2f} (증가)")
    
    drive = engine.get_current_drive()
    print(f"현재 욕구: {drive.drive_type.value}")
    print(f"메시지: {drive.message}")
    
    # 7. 수면 테스트
    print("\n[7] 수면 테스트")
    print("-" * 40)
    engine.state.energy = 0.3  # 에너지 낮춤
    
    print(engine.start_sleep())
    result = engine.sleep_cycle(cycles=10)
    print(result)
    print(engine.wake_up())
    
    state = engine.get_state()
    print(f"에너지: {state['internal_state']['energy']:.2f} (회복)")
    
    # 8. 최종 상태
    print("\n[8] 최종 상태")
    print("-" * 40)
    state = engine.get_state()
    print(f"내부 상태: {state['internal_state']}")
    print(f"현재 욕구: {state['current_drive']}")
    print(f"통계: {state['stats']}")
    
    print("\n" + "=" * 60)
    print("✅ 예제 완료!")
    print("=" * 60)


if __name__ == '__main__':
    main()

