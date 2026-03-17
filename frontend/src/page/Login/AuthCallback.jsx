// AuthCallback.js (새로운 컴포넌트)
import React, { useEffect } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';

const AuthCallback = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    console.log('asdf');
    const params = new URLSearchParams(location.search);
    const token = params.get('token');

    if (token) {
      localStorage.setItem('aura_token', token);
      console.log('✅ 토큰 저장 완료!');
      navigate('/'); // 또는 '/profile'
    } else {
      alert('로그인에 실패했습니다.');
      navigate('/login');
    }

    if (token) {
      localStorage.setItem('aura_token', token);
      console.log('로그인 성공! 토큰 저장됨:', token); // 이 로그가 찍히는지 확인
      navigate('/');
    } else {
      console.error('로그인 실패: 토큰이 없습니다.');
      navigate('/login');
    }
  }, [location, navigate]);

  return <div>로그인 처리 중입니다...</div>;
};

export default AuthCallback;
