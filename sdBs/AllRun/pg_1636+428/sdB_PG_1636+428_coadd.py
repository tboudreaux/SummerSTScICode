from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[249.532083,42.7492],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_PG_1636+428/sdB_PG_1636+428_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_PG_1636+428/sdB_PG_1636+428_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
