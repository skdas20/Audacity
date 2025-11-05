import React from 'react'

export default function Home() {
  return (
    <main style={{padding: 24, fontFamily: 'Arial, sans-serif'}}>
      <h1>Audacia (scaffold)</h1>
      <p>This is a minimal frontend scaffold. Connect to the backend at <code>/api</code>.</p>
      <ul>
        <li><a href="/realtime">Realtime VC UI (placeholder)</a></li>
        <li><a href="/tts">TTS UI (placeholder)</a></li>
        <li><a href="/replace">Replace UI (placeholder)</a></li>
      </ul>
    </main>
  )
}
