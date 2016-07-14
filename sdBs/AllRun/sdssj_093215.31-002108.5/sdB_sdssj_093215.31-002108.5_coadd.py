from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[143.063792,0.352361],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_093215.31-002108.5/sdB_sdssj_093215.31-002108.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_093215.31-002108.5/sdB_sdssj_093215.31-002108.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
