@test "Show statements for cat should specify an expression." {
    run grep -riI "show cat$"
    [ "${output}" = "" ]
}
@test "Show statements for sil should specify an expression." {
    run grep -riI "show sil$"
    [ "${output}" = "" ]
}
@test "Show statements for air should specify an expression." {
    run grep -riI "show air$"
    [ "${output}" = "" ]
}
