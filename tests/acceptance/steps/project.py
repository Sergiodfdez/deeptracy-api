from sqlalchemy import text
from behave import given, then, when

from tests.acceptance.utils import clean_db


@given(u'an empty project table in database')
def step_impl(context):
    clean_db(context)


@then(u'{created} projects are in the database')
def step_impl(context, created):
    sql = text('SELECT * FROM project')
    results = context.engine.execute(sql).fetchall()

    assert len(results) == int(created)


@given(u'a database with a project created')
def step_impl(context):
    sql = text('DELETE FROM project')
    context.engine.execute(sql)


@when(u'a project with id "{project_id}" exists in the database')
def step_impl(context, project_id):
    sql = text('INSERT INTO project (id, repo, hook_data, hook_type) VALUES (:id, :repo, \'\', \'\')')
    context.engine.execute(sql, id=project_id, repo='http://test{}.com'.format(project_id))


@then(u'project with id "{project_id}" is not in the database')
def step_impl(context, project_id):
    sql = text('SELECT * FROM project WHERE project.id = \'{}\''.format(project_id))
    results = context.engine.execute(sql).fetchall()

    assert len(results) == 0


@then(u'table projects is empty')
def step_impl(context):
    sql = text('SELECT * FROM project')
    results = context.engine.execute(sql).fetchall()

    assert len(results) == 0


@when(u'the user makes a "{method}" request to "/api/1/project/" endpoint')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user makes a "DELETE" request to "/api/1/project/" endpoint')


@when(u'the user makes a "GET" request to "<endpoint>" endpoint')
def step_impl(context):
    raise NotImplementedError(u'STEP: When the user makes a "GET" request to "<endpoint>" endpoint')
