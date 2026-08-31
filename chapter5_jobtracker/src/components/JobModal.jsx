import { useEffect, useState } from 'react'
import { STATUSES } from '../constants'

const emptyForm = {
  company: '',
  role: '',
  linkedinUrl: '',
  resume: '',
  dateApplied: new Date().toISOString().slice(0, 10),
  salary: '',
  notes: '',
  status: 'wishlist',
}

function isValidUrl(value) {
  try {
    new URL(value)
    return true
  } catch {
    return false
  }
}

export default function JobModal({ job, resumeOptions, onSave, onClose }) {
  const isEdit = Boolean(job)
  const [form, setForm] = useState(emptyForm)
  const [errors, setErrors] = useState({})

  useEffect(() => {
    if (job) {
      setForm({
        company: job.company || '',
        role: job.role || '',
        linkedinUrl: job.linkedinUrl || '',
        resume: job.resume || '',
        dateApplied: job.dateApplied || new Date().toISOString().slice(0, 10),
        salary: job.salary || '',
        notes: job.notes || '',
        status: job.status || 'wishlist',
      })
    } else {
      setForm(emptyForm)
    }
    setErrors({})
  }, [job])

  const set = (key) => (e) => setForm((f) => ({ ...f, [key]: e.target.value }))

  const handleSubmit = (e) => {
    e.preventDefault()
    const errs = {}
    if (!form.company.trim()) errs.company = 'Company name is required'
    if (!form.role.trim()) errs.role = 'Job title is required'
    if (form.linkedinUrl.trim() && !isValidUrl(form.linkedinUrl.trim()))
      errs.linkedinUrl = 'Enter a valid URL (including https://)'
    if (!form.dateApplied) errs.dateApplied = 'Date is required'
    setErrors(errs)
    if (Object.keys(errs).length > 0) return

    onSave({
      id: job?.id || crypto.randomUUID(),
      company: form.company.trim(),
      role: form.role.trim(),
      linkedinUrl: form.linkedinUrl.trim(),
      resume: form.resume.trim(),
      dateApplied: form.dateApplied,
      salary: form.salary.trim(),
      notes: form.notes.trim(),
      status: form.status,
      createdAt: job?.createdAt || new Date().toISOString(),
    })
  }

  const inputCls =
    'w-full rounded-lg border border-slate-300 bg-white px-3 py-2 text-sm text-slate-900 outline-none transition-colors focus:border-blue-500 focus:ring-2 focus:ring-blue-500/20 dark:border-slate-600 dark:bg-slate-800 dark:text-slate-100'
  const labelCls = 'mb-1 block text-xs font-medium text-slate-600 dark:text-slate-300'
  const errCls = 'mt-1 text-xs text-rose-500'

  return (
    <div
      className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 p-4 backdrop-blur-sm"
      onClick={onClose}
    >
      <div
        className="kanban-scroll max-h-[90vh] w-full max-w-lg overflow-y-auto rounded-2xl bg-white p-6 shadow-2xl dark:bg-slate-900"
        onClick={(e) => e.stopPropagation()}
      >
        <h2 className="mb-4 text-lg font-semibold text-slate-900 dark:text-slate-100">
          {isEdit ? 'Edit Job' : 'Add Job'}
        </h2>
        <form onSubmit={handleSubmit} noValidate>
          <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
            <div>
              <label className={labelCls}>Company *</label>
              <input className={inputCls} value={form.company} onChange={set('company')} />
              {errors.company && <p className={errCls}>{errors.company}</p>}
            </div>
            <div>
              <label className={labelCls}>Job Title / Role *</label>
              <input className={inputCls} value={form.role} onChange={set('role')} />
              {errors.role && <p className={errCls}>{errors.role}</p>}
            </div>
            <div className="sm:col-span-2">
              <label className={labelCls}>LinkedIn Job URL</label>
              <input
                className={inputCls}
                placeholder="https://www.linkedin.com/jobs/view/..."
                value={form.linkedinUrl}
                onChange={set('linkedinUrl')}
              />
              {errors.linkedinUrl && <p className={errCls}>{errors.linkedinUrl}</p>}
            </div>
            <div>
              <label className={labelCls}>Resume Used</label>
              <input
                className={inputCls}
                list="resume-options"
                placeholder="e.g. SDE_Resume_v3"
                value={form.resume}
                onChange={set('resume')}
              />
              <datalist id="resume-options">
                {resumeOptions.map((r) => (
                  <option key={r} value={r} />
                ))}
              </datalist>
            </div>
            <div>
              <label className={labelCls}>Date Applied *</label>
              <input
                type="date"
                className={inputCls}
                value={form.dateApplied}
                onChange={set('dateApplied')}
              />
              {errors.dateApplied && <p className={errCls}>{errors.dateApplied}</p>}
            </div>
            <div>
              <label className={labelCls}>Salary Range</label>
              <input
                className={inputCls}
                placeholder="e.g. ₹25-70 LPA"
                value={form.salary}
                onChange={set('salary')}
              />
            </div>
            <div>
              <label className={labelCls}>Status</label>
              <select className={inputCls} value={form.status} onChange={set('status')}>
                {STATUSES.map((s) => (
                  <option key={s.id} value={s.id}>
                    {s.label}
                  </option>
                ))}
              </select>
            </div>
            <div className="sm:col-span-2">
              <label className={labelCls}>Notes</label>
              <textarea
                className={`${inputCls} min-h-20 resize-y`}
                placeholder="Recruiter name, referral info, interview notes..."
                value={form.notes}
                onChange={set('notes')}
              />
            </div>
          </div>
          <div className="mt-6 flex justify-end gap-2">
            <button
              type="button"
              onClick={onClose}
              className="rounded-lg px-4 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 dark:text-slate-300 dark:hover:bg-slate-800"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="rounded-lg bg-blue-600 px-4 py-2 text-sm font-medium text-white shadow-sm hover:bg-blue-700"
            >
              {isEdit ? 'Save Changes' : 'Add Job'}
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
