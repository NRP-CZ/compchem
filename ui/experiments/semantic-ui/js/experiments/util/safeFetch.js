export const safeFetch = async (url, options = {}) => {
  try {
    const response = await fetch(url, options);
    if (!response.ok)
      console.error("Request failed:", response.status, response.statusText);

    let data;
    try {
      data = await response.json();
    } catch {
      data = null;
    }

    return { ok: response.ok, data };
  } catch (error) {
    console.error("Network error:", error);
    return { ok: false, data: null };
  }
};
