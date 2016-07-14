from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[240.3085,0.861544],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_pg_1558-007/sdB_pg_1558-007_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_pg_1558-007/sdB_pg_1558-007_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
