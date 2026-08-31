import { useMemo, useState } from 'react'
import {
  DndContext,
  DragOverlay,
  PointerSensor,
  useSensor,
  useSensors,
} from '@dnd-kit/core'
import { STATUSES } from '../constants'
import Column from './Column'
import JobCard from './JobCard'

export default function Board({ jobs, sortDesc, onStatusChange, onEdit, onDelete }) {
  const [activeJob, setActiveJob] = useState(null)
  const sensors = useSensors(
    useSensor(PointerSensor, { activationConstraint: { distance: 6 } }),
  )

  const byStatus = useMemo(() => {
    const sorted = [...jobs].sort((a, b) =>
      sortDesc
        ? (b.dateApplied || '').localeCompare(a.dateApplied || '')
        : (a.dateApplied || '').localeCompare(b.dateApplied || ''),
    )
    const map = Object.fromEntries(STATUSES.map((s) => [s.id, []]))
    for (const job of sorted) {
      if (map[job.status]) map[job.status].push(job)
    }
    return map
  }, [jobs, sortDesc])

  const handleDragEnd = (event) => {
    setActiveJob(null)
    const { active, over } = event
    if (!over) return
    const newStatus = over.id
    const job = jobs.find((j) => j.id === active.id)
    if (job && job.status !== newStatus) {
      onStatusChange(job, newStatus)
    }
  }

  return (
    <DndContext
      sensors={sensors}
      onDragStart={({ active }) => setActiveJob(jobs.find((j) => j.id === active.id) || null)}
      onDragEnd={handleDragEnd}
      onDragCancel={() => setActiveJob(null)}
    >
      <div className="kanban-scroll flex h-full gap-4 overflow-x-auto px-6 pb-4">
        {STATUSES.map((status) => (
          <Column
            key={status.id}
            status={status}
            jobs={byStatus[status.id]}
            onEdit={onEdit}
            onDelete={onDelete}
          />
        ))}
      </div>
      <DragOverlay>
        {activeJob ? <JobCard job={activeJob} onEdit={() => {}} onDelete={() => {}} overlay /> : null}
      </DragOverlay>
    </DndContext>
  )
}
