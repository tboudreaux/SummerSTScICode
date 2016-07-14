from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[72.774,17.530225],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_04482+1727/sdB_KUV_04482+1727_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_04482+1727/sdB_KUV_04482+1727_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
