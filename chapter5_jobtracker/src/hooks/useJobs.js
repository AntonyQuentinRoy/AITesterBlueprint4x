import { useCallback, useEffect, useState } from 'react'
import { getAllJobs, putJob, deleteJob, replaceAllJobs } from '../db'
import { seedJobs } from '../seedData'

export function useJobs() {
  const [jobs, setJobs] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getAllJobs()
      .then(async (rows) => {
        if (rows.length === 0 && !localStorage.getItem('jt-seeded')) {
          await replaceAllJobs(seedJobs)
          localStorage.setItem('jt-seeded', '1')
          setJobs(seedJobs)
        } else {
          setJobs(rows)
        }
      })
      .finally(() => setLoading(false))
  }, [])

  const saveJob = useCallback(async (job) => {
    await putJob(job)
    setJobs((prev) => {
      const idx = prev.findIndex((j) => j.id === job.id)
      if (idx === -1) return [...prev, job]
      const next = [...prev]
      next[idx] = job
      return next
    })
  }, [])

  const removeJob = useCallback(async (id) => {
    await deleteJob(id)
    setJobs((prev) => prev.filter((j) => j.id !== id))
  }, [])

  const importJobs = useCallback(async (incoming) => {
    await replaceAllJobs(incoming)
    setJobs(incoming)
  }, [])

  return { jobs, loading, saveJob, removeJob, importJobs }
}
