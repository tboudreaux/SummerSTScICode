from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[212.817333,-30.884375],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_CD-30_11223/sdB_CD-30_11223_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_CD-30_11223/sdB_CD-30_11223_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
