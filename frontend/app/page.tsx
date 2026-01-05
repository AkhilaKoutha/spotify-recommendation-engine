type Track = {
    id: string;
    name: string;
    artist: string;
    energy: number;
    valence: number;
    danceability: number;
    tempo: number;
};

async function getTracks(): Promise<Track[]> {
    const res = await fetch("http://backend:8000/tracks", {
        cache: "no-store",
    });

    if (!res.ok) {
        throw new Error("Failed to fetch tracks");
    }

    return res.json();
}

export default async function HomePage() {
    const tracks = await getTracks();

    return (
        <div>
            <h2>Tracks</h2>
            <ul>
                {tracks.map((track) => (
                    <li key={track.id} style={{ marginBottom: 12 }}>
                        <strong>{track.name}</strong> — {track.artist}
                        <div style={{ fontSize: 12, color: "#555" }}>
                            Energy: {track.energy} | Valence: {track.valence} | Tempo:{" "}
                            {track.tempo}
                        </div>
                    </li>
                ))}
            </ul>
        </div>
    );
}
