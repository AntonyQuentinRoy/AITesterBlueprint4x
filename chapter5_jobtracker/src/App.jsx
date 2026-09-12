import { useEffect, useMemo, useRef, useState } from 'react'
import { useJobs } from './hooks/useJobs'
import Board from './components/Board'
import JobModal from './components/JobModal'
import ConfirmDialog from './components/ConfirmDialog'

function useDarkMode() {
  const [dark, setDark] = useState(() => localStorage.getItem('jt-theme') === 'dark')
  useEffect(() => {
    document.documentElement.classList.toggle('dark', dark)
    localStorage.setItem('jt-theme', dark ? 'dark' : 'light')
  }, [dark])
  return [dark, setDark]
}

export default function App() {
  const { jobs, loading, saveJob, removeJob, replaceJobs, mergeJobs } = useJobs()
  const [dark, setDark] = useDarkMode()
  const [search, setSearch] = useState('')
  const [sortDesc, setSortDesc] = useState(true)
  const [modalJob, setModalJob] = useState(undefined) // undefined=closed, null=new, job=edit
  const [deletingJob, setDeletingJob] = useState(null)
  const [importData, setImportData] = useState(null)
  const fileInputRef = useRef(null)

  const filteredJobs = useMemo(() => {
    const q = search.trim().toLowerCase()
    if (!q) return jobs
    return jobs.filter(
      (j) => j.company.toLowerCase().includes(q) || j.role.toLowerCase().includes(q),
    )
  }, [jobs, search])

  const resumeOptions = useMemo(
    () => [...new Set(jobs.map((j) => j.resume).filter(Boolean))].sort(),
    [jobs],
  )

  const handleSave = async (job) => {
    await saveJob(job)
    setModalJob(undefined)
  }

  const handleStatusChange = (job, status) => saveJob({ ...job, status })

  const handleDelete = async () => {
    await removeJob(deletingJob.id)
    setDeletingJob(null)
  }

  const handleExport = () => {
    const blob = new Blob([JSON.stringify(jobs, null, 2)], { type: 'application/json' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `job-tracker-backup-${new Date().toISOString().slice(0, 10)}.json`
    document.body.appendChild(a)
    a.click()
    a.remove()
    setTimeout(() => URL.revokeObjectURL(url), 0)
  }

  const handleImport = async (e) => {
    const file = e.target.files?.[0]
    e.target.value = ''
    if (!file) return
    try {
      const data = JSON.parse(await file.text())
      if (!Array.isArray(data) || data.some((j) => !j.id || !j.company || !j.role || !j.status)) {
        alert('Invalid backup file: expected an array of job entries.')
        return
      }
      setImportData(data)
    } catch {
      alert('Could not read that file as JSON.')
    }
  }

  const handleImportMerge = async () => {
    await mergeJobs(importData)
    setImportData(null)
  }

  const handleImportReplace = async () => {
    await replaceJobs(importData)
    setImportData(null)
  }

  const iconBtn =
    'rounded-lg border border-slate-200 p-2 text-slate-500 transition-colors hover:bg-slate-100 hover:text-slate-700 dark:border-slate-700 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-slate-200'

  return (
    <div className="flex h-full flex-col bg-slate-50 dark:bg-slate-950">
      <header className="flex flex-wrap items-center gap-3 border-b border-slate-200 bg-white/80 px-6 py-3 backdrop-blur dark:border-slate-800 dark:bg-slate-900/80">
        <h1 className="text-base font-bold tracking-tight text-slate-900 dark:text-slate-100">
          Job Tracker
        </h1>
        <span className="rounded-full bg-blue-50 px-2 py-0.5 text-xs font-medium text-blue-700 dark:bg-blue-950 dark:text-blue-300">
          {search.trim()
            ? `${filteredJobs.length} of ${jobs.length} jobs`
            : `${jobs.length} jobs`}
        </span>

        <div className="relative ml-auto">
          <svg
            viewBox="0 0 20 20"
            fill="currentColor"
            className="pointer-events-none absolute left-3 top-1/2 h-4 w-4 -translate-y-1/2 text-slate-400"
          >
            <path
              fillRule="evenodd"
              d="M8 4a4 4 0 1 0 0 8 4 4 0 0 0 0-8zM2 8a6 6 0 1 1 10.89 3.476l4.817 4.817a1 1 0 0 1-1.414 1.414l-4.816-4.816A6 6 0 0 1 2 8z"
              clipRule="evenodd"
            />
          </svg>
          <input
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            placeholder="Search company or role..."
            className="w-56 rounded-lg border border-slate-200 bg-slate-50 py-2 pl-9 pr-3 text-sm outline-none transition-colors focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 dark:border-slate-700 dark:bg-slate-800 dark:text-slate-100"
          />
        </div>

        <button
          onClick={() => setSortDesc((v) => !v)}
          title={sortDesc ? 'Showing newest first' : 'Showing oldest first'}
          className={`${iconBtn} flex items-center gap-1.5 px-3 text-xs font-medium`}
        >
          <svg viewBox="0 0 20 20" fill="currentColor" className="h-3.5 w-3.5">
            <path d="M3 3a1 1 0 0 0 0 2h11a1 1 0 1 0 0-2H3zm0 4a1 1 0 1 0 0 2h7a1 1 0 1 0 0-2H3zm0 4a1 1 0 1 0 0 2h4a1 1 0 1 0 0-2H3zm12.293-4.707a1 1 0 0 1 1.414 0l2 2a1 1 0 0 1-1.414 1.414L16 8.414V16a1 1 0 1 1-2 0V8.414l-1.293 1.293a1 1 0 0 1-1.414-1.414l2-2a1 1 0 0 1 0 0z" />
          </svg>
          {sortDesc ? 'Newest' : 'Oldest'}
        </button>

        <button onClick={handleExport} title="Export all data as JSON" className={iconBtn}>
          <svg viewBox="0 0 20 20" fill="currentColor" className="h-4 w-4">
            <path
              fillRule="evenodd"
              d="M3 17a1 1 0 0 1 1-1h12a1 1 0 1 1 0 2H4a1 1 0 0 1-1-1zm3.293-7.707a1 1 0 0 1 1.414 0L9 10.586V3a1 1 0 1 1 2 0v7.586l1.293-1.293a1 1 0 1 1 1.414 1.414l-3 3a1 1 0 0 1-1.414 0l-3-3a1 1 0 0 1 0-1.414z"
              clipRule="evenodd"
            />
          </svg>
        </button>
        <button
          onClick={() => fileInputRef.current?.click()}
          title="Import JSON backup"
          className={iconBtn}
        >
          <svg viewBox="0 0 20 20" fill="currentColor" className="h-4 w-4">
            <path
              fillRule="evenodd"
              d="M3 17a1 1 0 0 1 1-1h12a1 1 0 1 1 0 2H4a1 1 0 0 1-1-1zM6.293 6.707a1 1 0 0 1 0-1.414l3-3a1 1 0 0 1 1.414 0l3 3a1 1 0 0 1-1.414 1.414L11 5.414V13a1 1 0 1 1-2 0V5.414L7.707 6.707a1 1 0 0 1-1.414 0z"
              clipRule="evenodd"
            />
          </svg>
        </button>
        <input
          ref={fileInputRef}
          type="file"
          accept="application/json"
          className="hidden"
          onChange={handleImport}
        />

        <button
          onClick={() => setDark((v) => !v)}
          title={dark ? 'Switch to light mode' : 'Switch to dark mode'}
          className={iconBtn}
        >
          {dark ? (
            <svg viewBox="0 0 20 20" fill="currentColor" className="h-4 w-4">
              <path
                fillRule="evenodd"
                d="M10 2a1 1 0 0 1 1 1v1a1 1 0 1 1-2 0V3a1 1 0 0 1 1-1zm4 8a4 4 0 1 1-8 0 4 4 0 0 1 8 0zm-.464 4.95.707.707a1 1 0 0 0 1.414-1.414l-.707-.707a1 1 0 0 0-1.414 1.414zm2.12-10.607a1 1 0 0 1 0 1.414l-.706.707a1 1 0 1 1-1.414-1.414l.707-.707a1 1 0 0 1 1.414 0zM17 11a1 1 0 1 0 0-2h-1a1 1 0 1 0 0 2h1zm-7 4a1 1 0 0 1 1 1v1a1 1 0 1 1-2 0v-1a1 1 0 0 1 1-1zM5.05 6.464A1 1 0 1 0 6.465 5.05l-.708-.707a1 1 0 0 0-1.414 1.414l.707.707zm1.414 8.486-.707.707a1 1 0 0 1-1.414-1.414l.707-.707a1 1 0 0 1 1.414 1.414zM4 11a1 1 0 1 0 0-2H3a1 1 0 0 0 0 2h1z"
                clipRule="evenodd"
              />
            </svg>
          ) : (
            <svg viewBox="0 0 20 20" fill="currentColor" className="h-4 w-4">
              <path d="M17.293 13.293A8 8 0 0 1 6.707 2.707a8.001 8.001 0 1 0 10.586 10.586z" />
            </svg>
          )}
        </button>

        <button
          onClick={() => setModalJob(null)}
          className="flex items-center gap-1.5 rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm transition-colors hover:bg-blue-700"
        >
          <svg viewBox="0 0 20 20" fill="currentColor" className="h-4 w-4">
            <path
              fillRule="evenodd"
              d="M10 3a1 1 0 0 1 1 1v5h5a1 1 0 1 1 0 2h-5v5a1 1 0 1 1-2 0v-5H4a1 1 0 1 1 0-2h5V4a1 1 0 0 1 1-1z"
              clipRule="evenodd"
            />
          </svg>
          Add Job
        </button>
      </header>

      <main className="min-h-0 flex-1 pt-4">
        {loading ? (
          <div className="flex h-full items-center justify-center text-sm text-slate-400">
            Loading your jobs...
          </div>
        ) : (
          <Board
            jobs={filteredJobs}
            sortDesc={sortDesc}
            onStatusChange={handleStatusChange}
            onEdit={(job) => setModalJob(job)}
            onDelete={setDeletingJob}
          />
        )}
      </main>

      {modalJob !== undefined && (
        <JobModal
          job={modalJob}
          resumeOptions={resumeOptions}
          onSave={handleSave}
          onClose={() => setModalJob(undefined)}
        />
      )}
      {deletingJob && (
        <ConfirmDialog
          title="Delete this job?"
          message={`Remove "${deletingJob.role}" at ${deletingJob.company}? This cannot be undone.`}
          onConfirm={handleDelete}
          onCancel={() => setDeletingJob(null)}
        />
      )}
      {importData && (
        <ConfirmDialog
          title="Import jobs?"
          message={`The file contains ${importData.length} jobs. Merge adds them to your existing ${jobs.length}; Replace all deletes your current jobs and keeps only the file.`}
          confirmLabel="Replace all"
          onConfirm={handleImportReplace}
          altLabel="Merge"
          onAlt={handleImportMerge}
          onCancel={() => setImportData(null)}
        />
      )}
    </div>
  )
}
