from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[217.48625,56.529528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SBSS_1428+567/sdB_SBSS_1428+567_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SBSS_1428+567/sdB_SBSS_1428+567_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
