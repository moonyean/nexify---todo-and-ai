import axiosInstance from "./axios";
import request from "../constant/request";

export const fetchProfile = async () => {
  const res = await axiosInstance.get(request.USER_PROFILE);
  return res.data;
};

export const updateSettings = async (settings) => {
  const res = await axiosInstance.patch(request.USER_SETTINGS, settings);
  return res.data;
};
