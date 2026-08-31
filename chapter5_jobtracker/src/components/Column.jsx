import { useDroppable } from '@dnd-kit/core'
import JobCard from './JobCard'

export default function Column({ status, jobs, onEdit, onDelete }) {
  const { setNodeRef, isOver } = useDroppable({ id: status.id })

  return (
    <div className="flex w-72 shrink-0 flex-col">
      <div className="mb-3 flex items-center gap-2 px-1">
        <span className="h-2.5 w-2.5 rounded-full" style={{ backgroundColor: status.accent }} />
        <h2 className="text-sm font-semibold text-slate-700 dark:text-slate-200">{status.label}</h2>
        <span className={`rounded-full px-2 py-0.5 text-xs font-semibold ${status.badge}`}>
          {jobs.length}
        </span>
      </div>
      <div
        ref={setNodeRef}
        className={`kanban-scroll flex flex-1 flex-col gap-2 overflow-y-auto rounded-xl p-1.5 transition-colors ${
          isOver ? status.columnOver : status.column
        }`}
      >
        {jobs.map((job) => (
          <JobCard key={job.id} job={job} onEdit={onEdit} onDelete={onDelete} />
        ))}
        {jobs.length === 0 && (
          <p className="py-8 text-center text-xs text-slate-400 dark:text-slate-500">
            Drop cards here
          </p>
        )}
      </div>
    </div>
  )
}
