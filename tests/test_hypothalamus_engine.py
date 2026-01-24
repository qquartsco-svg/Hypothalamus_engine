"""
Hypothalamus Engine Unit Tests
시상하부 엔진 단위 테스트

Author: GNJz (Qquarts)
Version: 1.0.0-alpha
"""

import unittest
import time
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'package'))

from hypothalamus import HypothalamusEngine, HypothalamusConfig, DriveType


class TestHypothalamusEngine(unittest.TestCase):
    """시상하부 엔진 테스트"""
    
    def setUp(self):
        """테스트 전 초기화"""
        self.config = HypothalamusConfig()
        self.engine = HypothalamusEngine(self.config)
    
    def test_initial_state(self):
        """초기 상태 테스트"""
        state = self.engine.get_state()
        
        # 초기 에너지는 1.0
        self.assertAlmostEqual(self.engine.state.energy, 1.0, places=2)
        
        # 초기 도파민은 0.5
        self.assertAlmostEqual(self.engine.state.dopamine, 0.5, places=2)
        
        # 초기 지루함은 0.0
        self.assertAlmostEqual(self.engine.state.boredom, 0.0, places=2)
    
    def test_energy_decay(self):
        """에너지 감쇠 테스트"""
        initial_energy = self.engine.state.energy
        
        # 활동 시뮬레이션 (10틱)
        for _ in range(10):
            self.engine.tick(action_type='think', stimulus_level=0.3)
        
        # 에너지가 감소했는지 확인
        self.assertLess(self.engine.state.energy, initial_energy)
    
    def test_energy_recovery(self):
        """에너지 회복 테스트"""
        # 에너지를 낮춤
        self.engine.state.energy = 0.3
        
        # 수면 시뮬레이션
        self.engine.tick(action_type='sleep', stimulus_level=0.0)
        
        # 에너지가 증가했는지 확인
        self.assertGreater(self.engine.state.energy, 0.3)
    
    def test_boredom_increase(self):
        """지루함 증가 테스트"""
        initial_boredom = self.engine.state.boredom
        
        # 대기 시뮬레이션 (자극 없음)
        for _ in range(30):
            self.engine.tick(action_type='idle', stimulus_level=0.0)
        
        # 지루함이 증가했는지 확인
        self.assertGreater(self.engine.state.boredom, initial_boredom)
    
    def test_boredom_decrease(self):
        """지루함 감소 테스트"""
        # 지루함을 높임
        self.engine.state.boredom = 0.8
        
        # 자극 있음 시뮬레이션
        self.engine.tick(action_type='chat', stimulus_level=0.9)
        
        # 지루함이 감소했는지 확인
        self.assertLess(self.engine.state.boredom, 0.8)
    
    def test_reward_system(self):
        """보상 시스템 테스트"""
        initial_dopamine = self.engine.state.dopamine
        
        # 보상 수신
        dopamine_gain = self.engine.receive_reward('praise', intensity=0.8)
        
        # 도파민이 증가했는지 확인
        self.assertGreater(self.engine.state.dopamine, initial_dopamine)
        self.assertGreater(dopamine_gain, 0.0)
    
    def test_drive_detection(self):
        """욕구 감지 테스트"""
        # 에너지를 낮춤
        self.engine.state.energy = 0.15
        
        # 현재 욕구 확인
        drive = self.engine.get_current_drive()
        
        # 수면 욕구가 감지되었는지 확인
        self.assertEqual(drive.drive_type, DriveType.SLEEP)
        self.assertGreater(drive.urgency, 0.5)
    
    def test_arousal_level(self):
        """각성 수준 테스트"""
        arousal = self.engine.get_arousal_level()
        
        # 각성 수준은 0.0 ~ 1.0 범위
        self.assertGreaterEqual(arousal, 0.0)
        self.assertLessEqual(arousal, 1.0)
    
    def test_sleep_cycle(self):
        """수면 사이클 테스트"""
        # 에너지를 낮춤
        self.engine.state.energy = 0.3
        
        # 수면 시작
        self.engine.start_sleep()
        
        # 수면 사이클 실행
        result = self.engine.sleep_cycle(cycles=5)
        
        # 에너지가 회복되었는지 확인
        self.assertGreater(self.engine.state.energy, 0.3)
        
        # 수면 카운트 증가 확인
        self.assertEqual(self.engine.stats['sleep_count'], 1)
    
    def test_state_clamping(self):
        """상태 값 범위 제한 테스트"""
        # 에너지를 범위 밖으로 설정
        self.engine.state.energy = 1.5
        self.engine.state.dopamine = -0.5
        
        # Clamping 적용
        self.engine._clamp_state()
        
        # 값이 0~1 범위로 제한되었는지 확인
        self.assertLessEqual(self.engine.state.energy, 1.0)
        self.assertGreaterEqual(self.engine.state.energy, 0.0)
        self.assertLessEqual(self.engine.state.dopamine, 1.0)
        self.assertGreaterEqual(self.engine.state.dopamine, 0.0)
    
    def test_custom_config(self):
        """커스텀 설정 테스트"""
        # 커스텀 설정 생성
        custom_config = HypothalamusConfig(
            energy_decay=0.01,  # 더 빠른 에너지 소모
            curiosity_weight=2.0  # 호기심 가중치 증가
        )
        
        custom_engine = HypothalamusEngine(custom_config)
        
        # 설정이 적용되었는지 확인
        self.assertEqual(custom_engine.config.energy_decay, 0.01)
        self.assertEqual(custom_engine.config.curiosity_weight, 2.0)


if __name__ == '__main__':
    unittest.main()

