from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[281.63562,14.087083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ_011506.17+140513.5/sdB_SDSSJ_011506.17+140513.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ_011506.17+140513.5/sdB_SDSSJ_011506.17+140513.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
