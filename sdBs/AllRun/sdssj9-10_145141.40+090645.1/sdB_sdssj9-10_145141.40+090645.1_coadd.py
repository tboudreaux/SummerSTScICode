from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[222.9225,9.112528],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_145141.40+090645.1/sdB_sdssj9-10_145141.40+090645.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_145141.40+090645.1/sdB_sdssj9-10_145141.40+090645.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
