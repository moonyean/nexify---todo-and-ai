import axiosInstance from "./axios";
import request from "../constant/request";

export const postSend = async (content) => {
  const res = await axiosInstance.post(request.CHAT_SEND, { content });
  return res.data;
};

export const fetchChatHistory = async () => {
  const res = await axiosInstance.get(request.CHAT_HISTORY);
  return res.data;
};

export const fetchChatSuggestions = async () => {
  const res = await axiosInstance.get(request.CHAT_SUGGESTIONS);
  return res.data;
};
