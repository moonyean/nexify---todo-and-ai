import axiosInstance from './axios';
import request from '../constant/request';

export const fetchTasks = async (date = null) => {
  const params = date ? { date } : {};
  const res = await axiosInstance.get(request.TASKS, { params });
  return res.data;
};

export const toggleTaskDone = async (id) => {
  const res = await axiosInstance.patch(`${request.TASKS}${id}/done`);
  return res.data;
};

export const updateTask = async (id, updates) => {
  const res = await axiosInstance.patch(`${request.TASKS}${id}/`, updates);
  return res.data;
};
