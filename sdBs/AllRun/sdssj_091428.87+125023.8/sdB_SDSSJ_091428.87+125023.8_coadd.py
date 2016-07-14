from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[138.620292,12.839944],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_091428.87+125023.8/sdB_SDSSJ_091428.87+125023.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_091428.87+125023.8/sdB_SDSSJ_091428.87+125023.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
