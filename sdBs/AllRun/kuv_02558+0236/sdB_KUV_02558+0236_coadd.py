from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[44.610042,2.796867],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_KUV_02558+0236/sdB_KUV_02558+0236_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_KUV_02558+0236/sdB_KUV_02558+0236_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
