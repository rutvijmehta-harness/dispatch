def test_create_signal_instance(session, signal, case_severity, case_priority, user):
    from dispatch.signal.flows import create_signal_instance

    case_priority.default = True
    case_priority.project_id = signal.project_id

    case_severity.default = True
    case_severity.project_id = signal.project_id

    instance_data = {"variant": signal.variant}

    assert create_signal_instance(
        db_session=session,
        project=signal.project,
        signal_instance_data=instance_data,
        current_user=user,
    )
