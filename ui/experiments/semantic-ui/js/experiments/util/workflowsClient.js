import { safeFetch } from "./safeFetch";

const API_URL = "https://localhost:5000/api";

export const fetchAvailableWorkflows = async (files) => {
  const data = {
    files,
  };

  const response = await safeFetch(`${API_URL}/workflows/available`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return response;
};

export const createWorkflow = async (recordId, workflowName, files) => {
  const data = {
    recordId,
    name: workflowName,
    files,
  };

  const response = await safeFetch(`${API_URL}/workflows`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return response;
};

export const listRecordWorkflows = async (
  recordId,
  skip,
  limit,
  statusFilter,
) => {
  const API = `http://localhost:8062/api/v1/workflows/${recordId}/list`;
  const params = new URLSearchParams({
    skip: skip,
    limit: limit,
  });

  if (statusFilter.length > 0) {
    params.append('status', `(${statusFilter.join(", ")})`)
  }

  const response = await safeFetch(API + `?${params.toString()}`, {
    method: "GET",
  });

  return response;
};

export const fetchWorkflowDetail = async (workflowName) => {
  const API = `http://localhost:8062/api/v1/workflows/${workflowName}/detail`;

  const response = await safeFetch(API, {
    method: "GET",
  });

  return response;
};
