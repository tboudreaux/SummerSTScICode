from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[243.287792,72.771183],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1613+729/sdB_pg_1613+729_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1613+729/sdB_pg_1613+729_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
