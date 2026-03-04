import axiosInstance from "./axios";
import request from "../constant/request";

export const fetchInsights = async () => {
  const res = await axiosInstance.get(request.INSIGHTS);

  return res.data;
};
