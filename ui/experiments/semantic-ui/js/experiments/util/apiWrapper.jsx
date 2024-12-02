const API_URL = 'https://mdrepo.eu/api'


export const createRecord = async (community, simulations) => {
    const data = {
        'files': {'enabled': True},
        'parent' : {
            'communities': {'default': community}
        },
        'metadata': simulations,
    }

    const response = await fetch(
            `${API_URL}/experiments`,
            {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            }
        )
        .catch((error) => { console.error(error); });
    
    if (!response.ok) {
        console.error(response.statusText);
    }

    return response;
}


export const editRecord = async (simulations, recordId) => {
    const data = {
        'metadata': simulations,
    }

    const response = await fetch(
            `${API_URL}/experiments/${recordId}/draft`,
            {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            }
        )
        .catch((error) => { console.error(error); });

    if (!response.ok) {
        console.error(response.statusText);
    }

    return response;
}


export const uploadFileToRecord = async (file, recordId) => {
    const remoteFileName = file.name;
    const data = [{'key': remoteFileName}]

    // 1. Create file

    const createResponse = await fetch(
            `${API_URL}/experiments/${recordId}/draft/files`,
            {
                method: 'POST',
                body: JSON.stringify(data),
            }
        )
        .catch((error) => { console.error(error); });
    
    if (!createResponse.ok) {
        console.error(createResponse.statusText);
        return createResponse;
    }

    // 2. Upload file

    const uploadResponse = await fetch(
            `${API_URL}/experiments/${recordId}/draft/files/${remoteFileName}`,
            {
                method: 'PUT',
                body: file,
            }
        )
        .catch((error) => { console.error(error); });
    
    if (!uploadResponse.ok) {
        console.error(uploadResponse.statusText);
        return uploadResponse;
    }

    // 3. Commit file

    const commitResponse = await fetch(
            `${API_URL}/experiments/${recordId}/draft/files/${remoteFileName}/commit`,
            {
                method: 'POST',
            }
        )
        .catch((error) => { console.error(error); });
    
    if (!commitResponse.ok) {
        console.error(commitResponse.statusText);
    }

    return commitResponse;
}


export const deleteFileFromRecord = async (remoteFileName, recordId) => {

    const response = await fetch(
            `${API_URL}/experiments/${recordId}/draft/files/${remoteFileName}`,
            {
                method: 'DELETE',
            }
        )
        .catch((error) => { console.error(error); });

    if (!response.ok) {
        console.error(response.statusText);
    }

    return response;
}


export const publishRecord = async (recordId) => {
    const response = await fetch(
            `${API_URL}/experiments/${recordId}/draft/actions/publish`,
            {
                method: 'POST',
            }
        )
        .catch((error) => { console.error(error); });

    if (!response.ok) {
        console.error(response.statusText);
    }

    return response;
}
