$(function () {
    let buttons = [];

    if (typeof exportColumns !== 'undefined') {
        buttons = [{
            extend: 'excelHtml5',
            text: 'Export',
            className: 'me-3',
            title: '',
            action: function (e, dt, button, config) {
                let selectedRows = table.rows({selected: true}).count();

                if (selectedRows > 0) {
                    $.fn.dataTable.ext.buttons.excelHtml5.action.call(this, e, dt, button, $.extend({}, config, {
                        exportOptions: {
                            columns: exportColumns,
                            modifier: {
                                selected: true
                            }
                        }
                    }));
                } else {
                    $.fn.dataTable.ext.buttons.excelHtml5.action.call(this, e, dt, button, $.extend({}, config, {
                        exportOptions: {
                            columns: exportColumns,
                        }
                    }));
                }
            }
        }]
    }

    if (canDelete) {
        buttons.push({
            text: 'Delete',
            className: 'btn btn-danger me-3 d-none',
            action: function () {
                let selectedRows = table.rows({selected: true}).nodes();
                let ids = $.map(selectedRows, function (row) {
                    return $(row).data('pk');
                });

                triggerBulkDelete(ids);
            },
            attr: {
                id: 'delete-selected'
            }
        });
    }
    let table = $('#datatable').DataTable({
        select: {
            style: 'multi',
            selector: 'td:first-child .select-row'
        },
        columnDefs: [
            {
                targets: 0,
                orderable: false,
                className: 'select-checkbox'
            },
            {
                targets: ':visible',
                type: 'string',
            }
        ],
        searching: true,
        ordering: false,
        scrollX: true,
        scrollCollapse: true,
        buttons: buttons,
        initComplete: function () {
            if (typeof filterColumn !== 'undefined') {
                let statusColumn = this.api().column(filterColumn);
                let select = $('#status-filter');

                select.on('change', function () {
                    let val = $(this).val();
                    statusColumn.search(val ? val : '', true, false).draw();
                });
            }
        }
    });

    $('#dt-search-0').addClass('form-control form-control-solid w-250px ps-13').attr('placeholder', 'Search').appendTo('#search-bar');
    $('.dt-search').remove();

    table.buttons().container().children().prependTo('.datatable-toolbar');

    $('#select-all').on('click', function () {
        let rows = table.rows({'search': 'applied'}).nodes();

        $('input[type="checkbox"]', rows).prop('checked', this.checked);

        if (this.checked) {
            table.rows({'search': 'applied'}).select();
            $('#delete-selected').removeClass('d-none');
        } else {
            table.rows({'search': 'applied'}).deselect();
            $('#delete-selected').addClass('d-none');
        }
    });

    // Handle click on individual checkbox to select row
    $('#datatable tbody').on('change', 'input[type="checkbox"]', function () {
        let $row = $(this).closest('tr');
        let rowIndex = table.row($row).index();

        if (this.checked) {
            table.row(rowIndex).select();
        } else {
            table.row(rowIndex).deselect();
        }

        let allCheckboxes = $('input[type="checkbox"]', table.rows({'search': 'applied'}).nodes());
        let checkedCheckboxes = $('input[type="checkbox"]:checked', table.rows({'search': 'applied'}).nodes());

        if (checkedCheckboxes.length === allCheckboxes.length) {
            $('#select-all').prop('checked', true).prop('indeterminate', false);
        } else if (checkedCheckboxes.length > 0) {
            $('#select-all').prop('checked', false).prop('indeterminate', true);
        } else {
            $('#select-all').prop('checked', false).prop('indeterminate', false);
        }

        if (checkedCheckboxes.length > 0) {
            $('#delete-selected').removeClass('d-none');
        } else {
            $('#delete-selected').addClass('d-none');
        }
    });

    function deleteSelectedRows(ids) {
        let form = document.createElement('form');
        form.method = 'POST';
        form.action = delete_url;

        let csrf_input = document.createElement('input');
        csrf_input.type = 'hidden';
        csrf_input.name = 'csrfmiddlewaretoken';
        csrf_input.value = csrf_token;

        form.appendChild(csrf_input);

        let input = document.createElement('input');
        input.type = 'hidden';
        input.name = 'ids';
        input.value = JSON.stringify(ids);

        form.appendChild(input);

        document.body.appendChild(form);
        form.submit();
    }

    let rowsToDelete;

    function setRowsToDelete(ids) {
        rowsToDelete = ids;
    }

    function triggerBulkDelete(ids) {
        setRowsToDelete(ids);
        $('#delete-modal').modal('show');
    }

    $(document).on('click', '.delete-action', function () {
        setRowsToDelete([$(this).closest('tr').data('pk')]);
        $('#delete-modal').modal('show');
    });

    $('#confirm-delete').on('click', function () {
        deleteSelectedRows(rowsToDelete);
        $('#delete-modal').modal('hide');
    });
})