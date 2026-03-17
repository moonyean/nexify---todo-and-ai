import api from './axiosInstance';
import { request } from '../constant/request';

export const googleLogin = async () => {
  window.location.href = 'http://127.0.0.1:8000/auth/login';
};

export const postLogout = async () => {
  const res = await api.post(request.AUTH_LOGOUT);
  return res.data;
};
