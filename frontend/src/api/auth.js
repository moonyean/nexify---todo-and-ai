import axiosInstance from "./axios";
import request from "../constant/request";

export const googleLogin = async () => {
  window.location.href = request.AUTH_LOGIN;
};

export const postLogout = async () => {
  const res = await axiosInstance.post(request.AUTH_LOGOUT);
  return res.data;
};
