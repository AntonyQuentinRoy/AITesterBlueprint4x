import { useDraggable } from '@dnd-kit/core'
import { STATUS_MAP, daysSince } from '../constants'

function LinkedInIcon() {
  return (
    <svg viewBox="0 0 24 24" fill="currentColor" className="h-4 w-4">
      <path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.55V9h3.57v11.45z" />
    </svg>
  )
}

export default function JobCard({ job, onEdit, onDelete, overlay = false }) {
  const { attributes, listeners, setNodeRef, isDragging } = useDraggable({
    id: job.id,
    disabled: overlay,
  })

  const status = STATUS_MAP[job.status]
  const days = daysSince(job.dateApplied)
  const stop = (e) => e.stopPropagation()

  return (
    <div
      ref={overlay ? undefined : setNodeRef}
      {...(overlay ? {} : { ...listeners, ...attributes })}
      style={{ borderLeftColor: status?.accent }}
      className={`group rounded-lg border border-l-4 border-slate-200 bg-white p-3 shadow-sm transition-shadow hover:shadow-md dark:border-slate-700 dark:bg-slate-800 ${
        isDragging ? 'opacity-40' : ''
      } ${overlay ? 'rotate-2 cursor-grabbing shadow-xl' : 'cursor-grab'}`}
    >
      <div className="flex items-start justify-between gap-2">
        <div className="min-w-0">
          <p className="truncate text-sm font-semibold text-slate-900 dark:text-slate-100">
            {job.company}
          </p>
          <p className="truncate text-xs text-slate-500 dark:text-slate-400">{job.role}</p>
        </div>
        {!overlay && (
          <div className="flex shrink-0 gap-1 opacity-0 transition-opacity group-hover:opacity-100">
            <button
              onPointerDown={stop}
              onClick={() => onEdit(job)}
              title="Edit"
              className="rounded p-1 text-slate-400 hover:bg-slate-100 hover:text-slate-600 dark:hover:bg-slate-700 dark:hover:text-slate-300"
            >
              <svg viewBox="0 0 20 20" fill="currentColor" className="h-3.5 w-3.5">
                <path d="M13.586 3.586a2 2 0 1 1 2.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793 3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
              </svg>
            </button>
            <button
              onPointerDown={stop}
              onClick={() => onDelete(job)}
              title="Delete"
              className="rounded p-1 text-slate-400 hover:bg-rose-50 hover:text-rose-600 dark:hover:bg-rose-950"
            >
              <svg viewBox="0 0 20 20" fill="currentColor" className="h-3.5 w-3.5">
                <path
                  fillRule="evenodd"
                  d="M9 2a1 1 0 0 0-.894.553L7.382 4H4a1 1 0 0 0 0 2v10a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2V6a1 1 0 1 0 0-2h-3.382l-.724-1.447A1 1 0 0 0 11 2H9zM7 8a1 1 0 0 1 2 0v6a1 1 0 1 1-2 0V8zm5-1a1 1 0 0 0-1 1v6a1 1 0 1 0 2 0V8a1 1 0 0 0-1-1z"
                  clipRule="evenodd"
                />
              </svg>
            </button>
          </div>
        )}
      </div>

      <div className="mt-2 flex flex-wrap items-center gap-1.5">
        {status && (
          <span className={`rounded-full px-2 py-0.5 text-[10px] font-semibold ${status.chip}`}>
            {status.label}
          </span>
        )}
        {job.resume && (
          <span className="rounded-full bg-slate-100 px-2 py-0.5 text-[10px] font-medium text-slate-600 dark:bg-slate-700 dark:text-slate-300">
            {job.resume}
          </span>
        )}
        {job.salary && (
          <span className="rounded-full border border-slate-200 px-2 py-0.5 text-[10px] font-medium text-slate-500 dark:border-slate-600 dark:text-slate-400">
            {job.salary}
          </span>
        )}
      </div>

      <div className="mt-2 flex items-center justify-between text-[11px] text-slate-400 dark:text-slate-500">
        <span>
          {days === null
            ? 'Not applied yet'
            : days === 0
              ? 'Applied today'
              : days === 1
                ? '1 day ago'
                : `${days} days ago`}
        </span>
        {job.linkedinUrl && (
          <a
            href={job.linkedinUrl}
            target="_blank"
            rel="noreferrer"
            onPointerDown={stop}
            onClick={stop}
            title="Open LinkedIn posting"
            className="text-[#0a66c2] hover:text-[#004182] dark:text-[#5aa9e6]"
          >
            <LinkedInIcon />
          </a>
        )}
      </div>
    </div>
  )
}
