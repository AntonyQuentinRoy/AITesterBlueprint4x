export const STATUSES = [
  {
    id: 'wishlist',
    label: 'Wishlist',
    accent: '#64748b',
    badge: 'bg-slate-200 text-slate-600 dark:bg-slate-700 dark:text-slate-300',
    column: 'bg-slate-100/70 dark:bg-slate-800/50',
    columnOver: 'bg-slate-200/80 dark:bg-slate-700/60',
    chip: 'bg-slate-100 text-slate-600 dark:bg-slate-700 dark:text-slate-300',
  },
  {
    id: 'applied',
    label: 'Applied',
    accent: '#3b82f6',
    badge: 'bg-blue-100 text-blue-700 dark:bg-blue-950 dark:text-blue-300',
    column: 'bg-blue-50/70 dark:bg-blue-950/30',
    columnOver: 'bg-blue-100/80 dark:bg-blue-900/40',
    chip: 'bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300',
  },
  {
    id: 'followup',
    label: 'Follow-up',
    accent: '#8b5cf6',
    badge: 'bg-violet-100 text-violet-700 dark:bg-violet-950 dark:text-violet-300',
    column: 'bg-violet-50/70 dark:bg-violet-950/30',
    columnOver: 'bg-violet-100/80 dark:bg-violet-900/40',
    chip: 'bg-violet-50 text-violet-700 dark:bg-violet-950 dark:text-violet-300',
  },
  {
    id: 'interview',
    label: 'Interview',
    accent: '#06b6d4',
    badge: 'bg-cyan-100 text-cyan-700 dark:bg-cyan-950 dark:text-cyan-300',
    column: 'bg-cyan-50/70 dark:bg-cyan-950/30',
    columnOver: 'bg-cyan-100/80 dark:bg-cyan-900/40',
    chip: 'bg-cyan-50 text-cyan-700 dark:bg-cyan-950 dark:text-cyan-300',
  },
  {
    id: 'offer',
    label: 'Offer',
    accent: '#22c55e',
    badge: 'bg-green-100 text-green-700 dark:bg-green-950 dark:text-green-300',
    column: 'bg-green-50/70 dark:bg-green-950/30',
    columnOver: 'bg-green-100/80 dark:bg-green-900/40',
    chip: 'bg-green-50 text-green-700 dark:bg-green-950 dark:text-green-300',
  },
  {
    id: 'rejected',
    label: 'Rejected',
    accent: '#ef4444',
    badge: 'bg-red-100 text-red-700 dark:bg-red-950 dark:text-red-300',
    column: 'bg-red-50/70 dark:bg-red-950/30',
    columnOver: 'bg-red-100/80 dark:bg-red-900/40',
    chip: 'bg-red-50 text-red-700 dark:bg-red-950 dark:text-red-300',
  },
  {
    id: 'onhold',
    label: 'On Hold',
    accent: '#eab308',
    badge: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-950 dark:text-yellow-300',
    column: 'bg-yellow-50/70 dark:bg-yellow-950/30',
    columnOver: 'bg-yellow-100/80 dark:bg-yellow-900/40',
    chip: 'bg-yellow-50 text-yellow-800 dark:bg-yellow-950 dark:text-yellow-300',
  },
]

export const STATUS_MAP = Object.fromEntries(STATUSES.map((s) => [s.id, s]))

export function daysSince(dateStr) {
  if (!dateStr) return null
  const then = new Date(dateStr + 'T00:00:00')
  const diff = Date.now() - then.getTime()
  return Math.max(0, Math.floor(diff / 86400000))
}
