const API_URL = 'https://mdrepo.eu/api'


const safeFetch = async (url, options = {}) => {
    try {
        const response = await fetch(url, options);
        if (!response.ok)
            console.error('Request failed:', response.status, response.statusText);

        let data;
        try {
            data = await response.json();
        } catch {
            data = null;
        }

        return { ok: response.ok, data };
    } catch (error) {
        console.error('Network error:', error);
        return { ok: false, data: null };
    }
};


export const createRecord = async (community, metadata) => {
    const data = {
        files: { enabled: true },
        parent: { communities: { default: community } },
        metadata: metadata,
    }

    const response = await safeFetch(
            `${API_URL}/experiments`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            }
        )

    return response;
}


export const editRecord = async (recordId, metadata) => {
    const data = {
        'metadata': metadata,
    }

    const response = await safeFetch(
            `${API_URL}/experiments/${recordId}/draft`,
            {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            }
        )

    return response;
}


export const listFilesOfRecord = async (recordId) => {
    return await safeFetch(
            `${API_URL}/experiments/${recordId}/draft/files`,
            {
                method: 'GET',
            }
        )
}


export const uploadFileToRecord = async (recordId, file) => {
    const remoteFileName = file.name;
    const data = [{'key': remoteFileName}]

    // Step 1/3: create file entry
    const createResponse = await safeFetch(
            `${API_URL}/experiments/${recordId}/draft/files`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            }
        )

    if (!createResponse.ok)
        return createResponse;

    // Step 2/3: upload file
    const uploadResponse = await safeFetch(
            `${API_URL}/experiments/${recordId}/draft/files/${remoteFileName}/content`,
            {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/octet-stream',
                },
                body: file,
            }
        )

    if (!uploadResponse.ok) {
        deleteFileFromRecord(recordId, remoteFileName);
        return uploadResponse;
    }

    // Step 3/3: commit file
    const commitResponse = await safeFetch(
            `${API_URL}/experiments/${recordId}/draft/files/${remoteFileName}/commit`,
            {
                method: 'POST',
            }
        )

    if (!commitResponse.ok)
        deleteFileFromRecord(recordId, remoteFileName);

    return commitResponse;
}


export const deleteFileFromRecord = async (recordId, remoteFileName) => {
    return await safeFetch(
            `${API_URL}/experiments/${recordId}/draft/files/${remoteFileName}`,
            {
                method: 'DELETE',
            }
        )
}


export const modifyFileInRecord = async (recordId, remoteFileName, file) => {
    const deleteResponse = await deleteFileFromRecord(recordId, remoteFileName);

    if (!deleteResponse.ok)
        return deleteResponse;

    return await uploadFileToRecord(recordId, file);
}


export const downloadFileFromRecord = async (recordId, remoteFileName, isDraft) => {
    const url = isDraft
        ? `${API_URL}/experiments/${recordId}/draft/files/${remoteFileName}/content`
        : `${API_URL}/experiments/${recordId}/files/${remoteFileName}/content`;

    let response = await fetch(url, { method: 'GET' })

    // draft only sends a direct URL to S3
    if (isDraft) {
        let newUrl = await response.text();
        console.log('Redirecting to:', newUrl);
        response = await fetch(newUrl, { method: 'GET' });
    }

    const blob = await response.blob();
    const file = new File([blob], remoteFileName, { type: blob.type });
    return file;
}


export const publishRecord = async (recordId) => {
    return await safeFetch(
            `${API_URL}/experiments/${recordId}/draft/actions/publish`,
            {
                method: 'POST',
            }
        )
}
