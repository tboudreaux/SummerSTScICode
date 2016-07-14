from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[71.171792,-5.460472],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_044441.23-052737.7/sdB_SDSSJ_044441.23-052737.7_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_044441.23-052737.7/sdB_SDSSJ_044441.23-052737.7_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
