from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[94.055542,22.763569],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_LSV+22_38/sdB_LSV+22_38_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_LSV+22_38/sdB_LSV+22_38_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
