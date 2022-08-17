	.file	"OptimizePractice.c"
	.text
	.globl	_operate
	.def	_operate;	.scl	2;	.type	32;	.endef
_operate:
LFB12:
	.cfi_startproc
	movl	8(%esp), %eax
	testb	$1, 4(%esp)
	je	L1
	addl	$1, (%eax)
L1:
	rep ret
	.cfi_endproc
LFE12:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "%d\12\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB13:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	pushl	%esi
	pushl	%ebx
	andl	$-16, %esp
	subl	$32, %esp
	.cfi_offset 6, -12
	.cfi_offset 3, -16
	call	___main
	movl	$0, 28(%esp)
	movl	$0, %ebx
	leal	28(%esp), %esi
L4:
	movl	%esi, 4(%esp)
	movl	%ebx, (%esp)
	call	_operate
	addl	$1, %ebx
	cmpl	$10, %ebx
	jne	L4
	movl	28(%esp), %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leal	-8(%ebp), %esp
	popl	%ebx
	.cfi_restore 3
	popl	%esi
	.cfi_restore 6
	popl	%ebp
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE13:
	.ident	"GCC: (MinGW.org GCC-6.3.0-1) 6.3.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
