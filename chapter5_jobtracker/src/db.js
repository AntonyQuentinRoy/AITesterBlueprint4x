import { openDB } from 'idb'

const DB_NAME = 'job-tracker-db'
const STORE = 'jobs'

const dbPromise = openDB(DB_NAME, 1, {
  upgrade(db) {
    db.createObjectStore(STORE, { keyPath: 'id' })
  },
})

export async function getAllJobs() {
  return (await dbPromise).getAll(STORE)
}

export async function putJob(job) {
  return (await dbPromise).put(STORE, job)
}

export async function deleteJob(id) {
  return (await dbPromise).delete(STORE, id)
}

export async function replaceAllJobs(jobs) {
  const db = await dbPromise
  const tx = db.transaction(STORE, 'readwrite')
  await tx.store.clear()
  await Promise.all(jobs.map((job) => tx.store.put(job)))
  return tx.done
}
