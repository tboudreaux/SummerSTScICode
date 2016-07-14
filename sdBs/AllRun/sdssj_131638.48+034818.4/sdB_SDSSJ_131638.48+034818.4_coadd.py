from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[199.160333,3.805111],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_131638.48+034818.4/sdB_SDSSJ_131638.48+034818.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_131638.48+034818.4/sdB_SDSSJ_131638.48+034818.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
