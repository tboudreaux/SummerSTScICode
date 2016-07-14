from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[77.963708,41.691428],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_RWT_114/sdB_RWT_114_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_RWT_114/sdB_RWT_114_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
