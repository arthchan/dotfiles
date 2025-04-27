return {
	{
		"lewis6991/gitsigns.nvim",
		config = function()
			require("gitsigns").setup({
				signs = {
					add = { text = "+" },
					change = { text = "~" },
					delete = { text = "_" },
					topdelete = { text = "-" },
					changedelete = { text = "~" },
					untracked = { text = "┆" },
				},
				signs_staged = {
					add = { text = "+" },
					change = { text = "~" },
					delete = { text = "_" },
					topdelete = { text = "‾" },
					changedelete = { text = "~" },
					untracked = { text = "┆" },
				},
				on_attach = function(bufnr)
					local gitsigns = require("gitsigns")

					local function map(mode, l, r, opts)
						opts = opts or {}
						opts.buffer = bufnr
						vim.keymap.set(mode, l, r, opts)
					end

					-- Navigation
					map("n", "[h", function()
						if vim.wo.diff then
							vim.cmd.normal({ "[h", bang = true })
						else
							gitsigns.nav_hunk("prev")
						end
					end, { desc = "Gitsigns: Go to previous hunk" })

					map("n", "]h", function()
						if vim.wo.diff then
							vim.cmd.normal({ "]h", bang = true })
						else
							gitsigns.nav_hunk("next")
						end
					end, { desc = "Gitsigns: Go to next hunk" })

					-- Actions
					map("n", "<leader>gb", function()
						gitsigns.blame_line({ full = true })
					end, { desc = "Gitsigns: Blame line" })
					map("n", "<leader>gd", gitsigns.diffthis, { desc = "Gitsigns: Diff this" })
					map("n", "<leader>gD", function()
						gitsigns.diffthis("~")
					end, { desc = "Gitsigns: Diff this ~" })
					map(
						"n",
						"<leader>gl",
						gitsigns.toggle_current_line_blame,
						{ desc = "Gitsigns: Toggle current line blame" }
					)
					map("n", "<leader>gp", gitsigns.preview_hunk, { desc = "Gitsigns: Preview hunk" })
					map("n", "<leader>gr", gitsigns.reset_hunk, { desc = "Gitsigns: Reset hunk in normal mode" })
					map("v", "<leader>gr", function()
						gitsigns.reset_hunk({ vim.fn.line("."), vim.fn.line("v") })
					end, { desc = "Gitsigns: Reset hunk in visual mode" })
					map("n", "<leader>gR", gitsigns.reset_buffer, { desc = "Gitsigns: Reset buffer" })
					map("n", "<leader>gs", gitsigns.stage_hunk, { desc = "Gitsigns: Stage hunk in normal mode" })
					map("v", "<leader>gs", function()
						gitsigns.stage_hunk({ vim.fn.line("."), vim.fn.line("v") })
					end, { desc = "Gitsigns: Stage hunk in visual mode" })
					map("n", "<leader>gS", gitsigns.stage_buffer, { desc = "Gitsigns: Stage buffer" })
					map("n", "<leader>gu", gitsigns.undo_stage_hunk, { desc = "Gitsigns: Undo stage hunk" })
					map("n", "<leader>gx", gitsigns.toggle_deleted, { desc = "Gitsigns: Toggle deleted" })

					-- Text object
					map({ "o", "x" }, "gh", ":<C-U>Gitsigns select_hunk<CR>", { desc = "Gitsigns: Select hunk" })
				end,
			})
		end,
	},
	{
		"tpope/vim-fugitive",
	},
}
