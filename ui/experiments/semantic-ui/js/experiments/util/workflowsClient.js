import { safeFetch } from "./safeFetch";

const API_URL = "https://localhost:5000/api";

export const runAllWorkflows = async (recordId, files) => {
  const data = {
    files,
  };

  const response = await safeFetch(`${API_URL}/workflows/${recordId}/all`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  return response;
};

export const fetchAvailableWorkflows = async (recordId, files) => {
  const data = {
    files,
  };

  const response = await safeFetch(
    `${API_URL}/workflows/${recordId}/available`,
    {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    },
  );

  return response;
};

export const createWorkflow = async (recordId, workflowName, files) => {
  const data = {
    recordId,
    name: workflowName,
    files,
  };

  const response = await safeFetch(`${API_URL}/workflows/${recordId}`, {
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
  const API = `${API_URL}/workflows/${recordId}/list`;
  const params = new URLSearchParams({
    skip: skip,
    limit: limit,
  });

  if (statusFilter.length > 0) {
    params.append("status", `(${statusFilter.join(", ")})`);
  }

  const response = await safeFetch(API + `?${params.toString()}`, {
    method: "GET",
  });

  return response;
};

export const fetchWorkflowDetail = async (recordId, workflowName) => {
  const API = `${API_URL}/workflows/${recordId}/${workflowName}/detail`;

  const response = await safeFetch(API, {
    method: "GET",
  });

  return response;
};

export const fetchWorkflowLogs = async (recordId, workflowName) => {
  const API = `${API_URL}/workflows/${recordId}/${workflowName}/logs`;

  const response = await safeFetch(API, {
    method: "GET",
  });

  return response;
};
