from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[259.254792,42.012722],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_171701.15+420045.8/sdB_sdssj_171701.15+420045.8_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_171701.15+420045.8/sdB_sdssj_171701.15+420045.8_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
